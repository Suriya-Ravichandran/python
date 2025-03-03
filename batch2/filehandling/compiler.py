from flask import Flask, request, render_template_string
import sys
import io

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""
    if request.method == "POST":
        user_code = request.form["code"]
        
        # Redirect stdout to capture print statements
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()

        try:
            # Execute the code entered by the user
            exec(user_code)
            output = sys.stdout.getvalue()
        except Exception as e:
            output = f"Error: {str(e)}"

        # Restore original stdout
        sys.stdout = old_stdout

    # Simple HTML interface to get the code from the user
    return render_template_string("""
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Python Online Compiler</title>
        </head>
        <body>
            <h1>Python Online Compiler</h1>
            <form method="POST">
                <textarea name="code" rows="10" cols="50">{{ request.form['code'] }}</textarea><br><br>
                <input type="submit" value="Run Code">
            </form>
            <h2>Output:</h2>
            <pre>{{ output }}</pre>
        </body>
        </html>
    """, output=output)


if __name__ == "__main__":
    app.run(debug=True)
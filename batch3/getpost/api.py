from flask import Flask, request, jsonify

app = Flask(__name__)

# Middleware for logging GET and POST requests
@app.before_request
def log_request():
    if request.method == 'GET':
        print(f"GET request received at {request.path} with params: {request.args}")
    elif request.method == 'POST':
        print(f"POST request received at {request.path} with body: {request.json or request.form}")

# Route for GET request
@app.route('/get_example', methods=['GET'])
def get_example():
    # You can access query parameters using request.args
    data = request.args  # To get query parameters (e.g., ?name=John&age=30)
    return jsonify({"message": "This is a GET request response", "data": data})


# Route for POST request
@app.route('/post_example', methods=['POST'])
def post_example():
    data = request.json or request.form
    return jsonify({"message": "POST request received", "data": data})

if __name__ == '__main__':
    app.run(debug=True)

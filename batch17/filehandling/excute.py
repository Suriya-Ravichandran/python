import subprocess

filename = input("Enter filename to run: ")

# Run the subprocess and capture output
result = subprocess.run(["python", filename], capture_output=True, text=True)

# Print standard output
print("Output:\n", result.stdout)

# Optionally, print errors if any
if result.stderr:
    print("Error:\n", result.stderr)

filename=str(input("Enter the name of the file to create: "))
try:
    with open(filename, 'w') as file:
        content=str(input("Enter the content to write in the file: "))
        file.write(content)
        print(f"Content written to file '{filename}' successfully.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

filename=str(input("Enter the name of the file to create: "))

try:
    with open(filename, 'x') as file:
         print(f"File '{filename}' created successfully.")
except FileExistsError:
    print(f"File '{filename}' already exists. Please choose a different name.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")
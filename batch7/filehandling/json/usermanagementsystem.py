import json

# Define the filename for the JSON file
filename = "user_data.json"

# Function to read existing data from the JSON file
def read_data():
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file does not exist

# Function to write data to the JSON file
def write_data(data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add new user data
def add_user():
    data = read_data()
    user_id = input("Enter User ID: ")
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    
    # Add user data to the dictionary
    data[user_id] = {"name": name, "email": email}
    
    write_data(data)
    print("User added successfully!")

# Function to delete user data
def delete_user():
    data = read_data()
    user_id = input("Enter the User ID to delete: ")
    
    if user_id in data:
        del data[user_id]
        write_data(data)
        print(f"User {user_id} deleted successfully!")
    else:
        print(f"User with ID {user_id} not found.")

# Function to access and display user data
def display_data():
    data = read_data()
    if not data:
        print("No user data available.")
    else:
        for user_id, user_info in data.items():
            print(f"User ID: {user_id}")
            print(f"Name: {user_info['name']}")
            print(f"Email: {user_info['email']}")
            print("-" * 20)

# Menu for user management system
def menu():
    while True:
        print("\nUser Management System")
        print("1. Add new user")
        print("2. Delete user")
        print("3. Display all users")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            add_user()
        elif choice == '2':
            delete_user()
        elif choice == '3':
            display_data()
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice, please try again.")

# Start the program by calling the menu function
if __name__ == "__main__":
    menu()

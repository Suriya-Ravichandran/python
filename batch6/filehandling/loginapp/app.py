import json

def signin():
    username = str(input("Enter your Username: "))
    password = str(input("Enter your Password: "))

    userdata = {}
    # Adding a new user to the dictionary
    userdata["user1"] = {"name": username, "password": password}
    
    # Open the file in write mode and use json.dump() to write the data as JSON
    with open("../file/userdata.json", "w") as f:
        json.dump(userdata, f, indent=4)

    print("User data saved to userdata.json")

signin()

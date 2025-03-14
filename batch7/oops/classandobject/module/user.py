class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def login(self, email, password):
        if self.email == email:
            if self.password == password:
                print("Login successful")
            else:
                print("Incorrect password")
        else:
            print("User not found")

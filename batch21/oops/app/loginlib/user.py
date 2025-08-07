class User:

    def __init__(self, name, email, password, bio):
        self.name = name
        self.email = email
        self.password = password
        self.bio = bio

    # Setter and Getter for name
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    # Setter and Getter for email
    def set_email(self, email):
        self.email = email

    def get_email(self):
        return self.email

    # Setter and Getter for password
    def set_password(self, password):
        self.password = password

    def get_password(self):
        return self.password

    # Setter and Getter for bio
    def set_bio(self, bio):
        self.bio = bio

    def get_bio(self):
        return self.bio
    


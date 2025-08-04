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
    

# testing 

# u1=User("foo","foo@gmail.com","foo@123","i am a foo")
# u2=User("boo","boo@gmail.com","boo@123","i am a boo")


# print(u1.get_name())
# print(u2.get_name())
# u1.set_name("hoo")
# print(u1.get_name())
# print(u1.get_email())
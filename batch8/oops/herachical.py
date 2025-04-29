class bike():
    def duke(self):
        print("Ready to race")

class person(bike):
    def scooter(self):
        print("Going only shops")

class child(person,bike):
    pass

ch1=child()
ch1.duke()
ch1.scooter()
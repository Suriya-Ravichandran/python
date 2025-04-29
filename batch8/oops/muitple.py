class bike():
    def duke(self):
        print("Ready to race")

class person(bike):
    def scooter(self):
        print("Going only shops")

class child(bike):
    pass


p1=person()

p1.duke()
p1.scooter()

ch1=child()
ch1.duke()
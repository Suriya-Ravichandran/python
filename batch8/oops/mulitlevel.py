class bike():
    def duke(self):
        print("Ready to race")

class person(bike):
    pass

class child(person):
    pass


p1=person()
p1.duke()

ch1=child()

ch1.duke()
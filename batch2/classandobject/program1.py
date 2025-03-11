class KTM:

    rc200="it is sports Bike"

    def duke200(self):
        print("Ready to Race")


deepak=KTM()
suriya=KTM()

suriya.duke200()
print("suriya:",id(suriya))
deepak.duke200()
print("deepak:",id(deepak))
print(deepak.rc200)
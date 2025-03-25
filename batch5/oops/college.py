class EEE:

    Dhanapriya="I am Dhanapriya ..."

    def dhanapriya(self):
        print(self)
        print("I am Dhanapriya ...")

class ECE(EEE):
    def unknown(self):
        print("I am Unknown")


staff=EEE()
staffECE=ECE()
staff2=EEE()
# print(id(staff))
# print(id(staff2))
# print(staff.Dhanapriya)
# print(staff2.Dhanapriya)


staff.dhanapriya()
staff2.dhanapriya()
staffECE.unknown()
staffECE.dhanapriya()



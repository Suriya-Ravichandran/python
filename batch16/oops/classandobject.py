class  BECS:

    student1="foo"
    student2="boo"

    def studying(self):
        print(self)
        print("Students prepare your test")


teachar=BECS()
teachar2=BECS()
print(teachar.student1)
teachar.studying()
teachar2.studying()
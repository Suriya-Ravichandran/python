# class Parent():
#     def money(self):
#         print("Take money")

# class Child(Parent):
#     def toy(self):
#         print("Playing with my toy")


# c1=Child()

# c1.money()
# c1.toy()



# multilevel

# class Grandparent():

#     def land(self):
#         print("Take my land")

# class Parent(Grandparent):
#     def money(self):
#         print("Take money")

# class Child(Parent):
#     def toy(self):
#         print("Playing with my toy")


# c1=Child()

# c1.land()
# c1.money()
# c1.toy()


# multiple

# class Grandparent():

#     def land(self):
#         print("Take my land")

# class Parent():
#     def money(self):
#         print("Take money")

# class Child(Parent,Grandparent):
#     def toy(self):
#         print("Playing with my toy")


# c1=Child()

# c1.land()
# c1.money()
# c1.toy()

# hechical 

class parent():

    def land(self):
        print("Take my land")

class child1(parent):
    def money(self):
        print("Take money")

class Child2(parent):
    def toy(self):
        print("Playing with my toy")


c1=child1()

c1.land()
c1.money()

c2=Child2()

c2.land()
c2.toy()



# there are four type
# single 
# muliple
# multi-level
# hierarchical


# class Parent:
#     def money(self):
#         print("take money !!")
    

# class child(Parent):
#     pass

# ch1=child()
# ch1.money()


# class Parent:
#     def money(self):
#         print("take money !!")
    

# class child(Parent):
#     pass

# class child2(Parent):
#     pass
# ch1=child()
# ch2=child2()
# ch1.money()
# ch2.money()


# class Parent:
#     def money(self):
#         print("take money !!")
    

# class child(Parent):
#      def dress(self):
#          print("New dress")

# class child2(child):
#     pass


# ch1=child()
# ch1.money()
# ch2=child2()
# ch2.money()
# ch2.dress()

class Head():
    def ceo(self):
        print("I am a ceo")

class manager(Head):
    def manager1(self):
        print("I am a manager 1")

class employee1(manager):
    def employee1(self):
        print("I am a employee 1")

class manager2(Head):
    def manager2(self):
        print("I am a manager 2")

class employee2(manager):
    def employee2(self):
        print("I am a employee 2")
class hello():
    def hello():
        print("Hello")


class hello2(hello):
    def hello2():
        print("hello2")


class hello3(hello2):
    def hello3():
        print("Hello3")

class hello4(hello2):
    def hello4():
        print("Hello4")


h4=hello4

h4.hello()

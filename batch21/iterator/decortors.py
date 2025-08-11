def decorator(func):
    def msg():
        print("first message")
        func()
        print("third message")
    return msg


@decorator
def greet():
    print("Second message")

greet()
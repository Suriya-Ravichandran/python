
def decorator(msg):
    def message():
        print("Hello")
        msg()
        print("bye")
    return message


@decorator
def greet():
    print("Welcome to livewire")


greet()

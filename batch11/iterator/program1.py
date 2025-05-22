# A simple decorator function
def decorator(func):
  
    def helloworld():
        func()
        print("Hello world")
       
    return helloworld

# Applying the decorator to a function
@decorator

def sumof():
    n=10
    n1=20
    print(f"sum of {n+n1}")


sumof()
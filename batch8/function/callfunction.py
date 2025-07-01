class Add:
    def __init__(self, label=None):
        self.label = label  # Optional: just storing some label or identifier

    def __call__(self, num1, num2):
        return num1 + num2  # Or print(num1 + num2) if you prefer
    
    def __call__(self, num1, num2):
        return num1 * num2

# Create an instance of Add
add = Add()
mul=Add()
# Call the instance like a function
result1 = add(10, 20)
result2 =mul(10,10)
print("Result:", result1)
print("Result:", result2)

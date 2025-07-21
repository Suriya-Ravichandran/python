class SuriyaError(Exception):
    pass

while True:
    num1 = int(input("Enter num1: "))
    num2 = int(input("Enter num2: "))
    if num1 == 0 or num2 == 0:
        raise SuriyaError("This suriya Custom error")
    else:
        result = num1 / num2
    print(f"Result: {result}")


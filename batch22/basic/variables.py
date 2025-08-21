# student bio app 

print("----Student bio App-----")

# get input from user
name=str(input("Enter your name: "))
age=int(input("Enter your age"))
dob=str(input("Enter your DOB: "))
mark10=float(input("Enter your 10th mark: "))
mark12=float(input("Enter your 12th mark: "))
percentage10=mark10/5
percentage12=mark12/6


# print a output

'''
this muli
line comment
'''


print("Name:",name)
print(f"Age: {age}")
print("DOB: "+dob)
print(f"10th mark: {mark10}")
print(f"12th mark: {mark12}")
print(f"10th Percentage:",percentage10)
print(f"12th Percentage:",percentage12)
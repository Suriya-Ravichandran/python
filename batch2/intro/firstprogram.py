# Bio Data app
# get input
Name=str(input("Enter your name: "))
Age=int(input("Enter your Age: "))
DateOfBirth=str(input("Enter your Date of Birth: "))
SSLC=float(input("Enter SSLC Mark: "))
Per_SSLC=SSLC/5
HSC=float(input("Enter HSC Mark: "))
Per_HSC=HSC/6

print("----------Student Bio Details------------")
print(f"Name: {Name}")
print(f"Age: {Age}")
print(f"Date of Birth: {DateOfBirth}")
print(f"SSLC Mark: {SSLC}")
print(f"Percentage of SSLC: {Per_SSLC}")
print(f"HSC Mark: {HSC}")
print(f"Percentage of HSC: {Per_HSC}")

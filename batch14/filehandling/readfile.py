filename=str(input("Enter the name of the file to create: "))
try:
    f=open(filename,'r')
    print(f.read())
except FileNotFoundError:
    print(f"File '{filename}' does not exist. Please create the file first.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")
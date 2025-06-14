filename=str(input("Enter the name of the file to create: "))
try:
    f=open(filename,'a')
    content=str(input("Enter the content to append to the file: "))
    f.write(content + '\n')
    print(f"Content appended to file '{filename}' successfully.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")


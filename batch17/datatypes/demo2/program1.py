def palindrome(text):
    orignal_text=text
    reverse_text=text[::-1]
    if orignal_text==reverse_text:
        return True
    else:
        return False

text=[]
hwd=int(input("How many text you want to add: "))
for x in range(hwd):
    data=str(input(f"Enter your {x+1} data: "))
    text.append(data)


result=filter(palindrome,text)
print("Palindrome:",list(result))


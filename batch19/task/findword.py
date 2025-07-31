data="racecar"

r=0
a=0
e=0

for x in data:

    if x=="r":
        r+=1
    elif x=="a":
        a+=1
    elif x=="e":
        e+=1

print(f"r ={r}")
print(f"a ={a}")
print(f"e ={e}")
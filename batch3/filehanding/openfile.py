# f=open("demo.txt","r")
# f=open("./file/demo.txt","r")
# print(f.read())
f=open("D:/html/box-model.html","r")
# print(f.read(500))
# print(f.readline())
i=0
for x in f:
   i+=1
   if i==3:
      print(x)
   elif i>=4:
        break
   
f.close()
  
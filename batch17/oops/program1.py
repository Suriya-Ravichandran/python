class mathamatics():
    def gen_table(self,table,times):
        print(self)
        result=0
        for x in range(1,times+1):
            result=table*x
            print(f"{table} x {times} = {result}")

    def square(*num):
        print(num)
        for x in range(1,len(num)):
            print(num[x]*num[x])


s1=mathamatics()
s2=mathamatics()
s1.gen_table(2,10)
s2.gen_table(4,10)

s1.square(10,30,40)
s2.square(40,50)
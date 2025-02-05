def recursion(value):
    if(value>0):
        # 1+0
           
           #21     #6        #15     #6
        result=value+recursion(value-1)   #6+5,5+4,4+3,3+2,2+1,1+0
                #1+0 =1 
                #2+1=3
                #3+3=6
                #4+6=10
                #5+10=15
                #6+15=21
    else:
        result=0
    return result

print("Recursion:")
#send the value
print(recursion(100))

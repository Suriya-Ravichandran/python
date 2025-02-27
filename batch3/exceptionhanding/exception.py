# try -  
# except
# else
# finally


while True:
    value1=int(input("Enter Value1:"))
    value2=int(input("Enter Value2:"))
    try:
      print(value1/value2)
    except:
       print("invaild operation divide by Zero")
    # else:
    #    print("No Error Found")

    finally:
       print("try and catch is executed successfully")

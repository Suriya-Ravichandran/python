def NameList( *name):
    print(len(name))
    for x in range(len(name)):
        print("Stutent No",x+1,":",name[x])



NameList("foo","boo","sachin","suriya")
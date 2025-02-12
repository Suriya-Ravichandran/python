examtime="10:00"
examdate="11-02-2025"

stime=str(input("Enter reach time: "))
sdate=str(input("Enter Exam Date: "))

if(examtime==stime and examdate==sdate):
    print("Go write")
elif(examtime!=stime and examdate==sdate):
    print("Go to Hell")
else:
    print("Exam not condected")
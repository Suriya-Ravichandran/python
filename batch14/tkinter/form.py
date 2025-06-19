from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("600x600")

# submit function
def submit():
    name=name_var.get()
    email=email_var.get()
    phoneno=phone_var.get()
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone No: {phoneno}")
   

# variables to store a data
name_var=StringVar()
email_var=StringVar()
phone_var=IntVar()
# widgets

# name field
namelabel=Label(window,text="Name",font=("Arial",10),).place(x=50,y=50)
namefield=Entry(window,font=("Normal",18),width=20,textvariable=name_var).place(x=50,y=80)

# email
emaillabel=Label(window,text="Email",font=("Arial",10),).place(x=50,y=120)
emailfield=Entry(window,font=("Normal",18),width=20,textvariable=email_var).place(x=50,y=150)

# phone no

phonelabel=Label(window,text="Phone No",font=("Arial",10),).place(x=50,y=190)
phonefield=Entry(window,font=("Normal",18),width=20,textvariable=phone_var).place(x=50,y=220)

btn=Button(window,text="Submit",height=2,width=14,bg="blue",fg="white",command=submit).place(x=50,y=270)


window.mainloop()
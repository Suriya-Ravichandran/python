from tkinter import *
from tkinter import messagebox
from tkinter import ttk
Window=Tk()
Window.geometry("600x600")                                


def submit():
    name=namevar.get()
    email=emailvar.get()
    password=passwordvar.get()
    gender=gendervar.get()
    hobby1=hobby1var.get()
    nation=nationvar.get()
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Gender: {gender}")
    print("---------Hobbies--------")
    print(f"cricket: {hobby1}")
    print(f"Nation: {nation}")
    messagebox.showinfo("Success","Form submit successfully")



namevar=StringVar()
emailvar=StringVar()
passwordvar=StringVar()
gendervar=StringVar()
gendervar.set("Male")
hobby1var=IntVar()
nationvar=StringVar()
nationvar.set("None")
nationoptions=[
    "India",
    "USA",
    "Russia",
    "China"
]



namelabel=Label(Window,text="Name",font=("bold",15)).place(x=50,y=50)
nameinput=Entry(Window,width=35,font=("normal",12),textvariable=namevar).place(x=50,y=80)
Emaillabel=Label(Window,text="Email",font=("bold",15)).place(x=50,y=100)
Emailinput=Entry(Window,width=35,font=("normal",12),textvariable=emailvar).place(x=50,y=130)
passwordlabel=Label(Window,text="Password",font=("bold",15)).place(x=50,y=150)
passwordinput=Entry(Window,width=35,font=("normal",12), show="*",textvariable=passwordvar).place(x=50,y=180)
genderinput=Radiobutton(Window,text="Male",value="Male",variable=gendervar).place(x=50,y=210)
genderinput1=Radiobutton(Window,text="Female",value="Female",variable=gendervar).place(x=100,y=210)
hobby1=Checkbutton(Window,variable=hobby1var,onvalue=1,offvalue=0,text="Cricket").place(x=50,y=240)

nation=ttk.Combobox(Window,values=nationoptions,textvariable=nationvar).place(x=50,y=270)


btn=Button(Window,text="submit",bg="blue",fg="white",height=1,width=12,command=submit).place(x=50,y=300)


Window.mainloop()
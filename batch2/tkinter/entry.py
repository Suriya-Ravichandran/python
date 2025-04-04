from tkinter import *

from tkinter import messagebox

window=Tk()

window.title("Button Example")
window.geometry("400x400")
window.configure(bg="grey")

# functions

def login():
    name=name_var.get()
    password=password_var.get()
    print("Name:",name)
    print("Password:",password)
    window.destroy()
    msg=messagebox.showinfo("Login Details",f"Name:{name},Password:{password}")



# datas
name_var=StringVar()
password_var=StringVar()

lable1=Label(window,text="Enter UserName",fg="red", font=("bold",10),bg="grey")
input1=Entry(window,textvariable=name_var,font=("normal",10))
lable2=Label(window,text="Enter Password",fg="red", font=("bold",10),bg="grey")
input2=Entry(window,textvariable=password_var,font=("normal",10),show="*")
btn1=Button(window,text="Login",fg="white",bg="black",command=login)



lable1.place(x=50,y=50)
input1.place(x=50,y=70)
lable2.place(x=50,y=100)
input2.place(x=50,y=120)
btn1.place(x=50,y=143)
window.mainloop()


from tkinter import *
import tkinter as tk

# window
window=tk.Tk()
window.title("Login")
window.geometry("450x450")

# events

def submit():
    name=name_var.get()
    password=password_var.get()
    gender=gender_var.get()
    print("Name:",name)
    print("Password:",password)
    print("Gender:",gender)


# lable, entry and btn creation
name_var=tk.StringVar()
password_var=tk.StringVar()

name_lable=tk.Label(window,text="Username",font=("bold",10))
name_entry=tk.Entry(window,textvariable=name_var,font=("normal",10))

password_lable=tk.Label(window,text="Password",font=("bold",10))
password_entry=tk.Entry(window,textvariable=password_var,font=("normal",10),show="*")

gender_var=tk.StringVar(window,"male")
radio_button1=tk.Radiobutton(window,text="Male",variable=gender_var,value="male")
radio_button2=tk.Radiobutton(window,text="Female",variable=gender_var,value="female")
 
submit_btn=tk.Button(window,text="submit",command=submit)


# set position of all widgets
name_lable.place(x=10,y=50)
name_entry.place(x=90,y=50)
password_lable.place(x=10,y=80)
password_entry.place(x=90,y=80)
radio_button1.place(x=10,y=120)
radio_button2.place(x=10,y=140)
submit_btn.place(x=110,y=200)
window.mainloop()
from tkinter import *
from tkinter import messagebox


window=Tk()
window.geometry("600x600")

def clickme():
    name=name_var.get()
    msg=messagebox.showinfo("information",f"Hello {name}")



name_var=StringVar()

input1=Entry(window,width=20,font=('Arial',18),textvariable=name_var).place(x=50,y=50)
btn=Button(window,text="click me",height=2,width=18,bg="blue",fg="white",command=clickme).place(x=50,y=100)

window.mainloop()
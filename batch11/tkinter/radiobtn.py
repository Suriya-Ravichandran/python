from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("New window")
window.geometry("600x600")


def clickme():
    data=data_var.get()
    gender=gender_var.get()
    print(data)
    print(gender)
    msg=messagebox.showwarning("information",data)


data_var=StringVar()
gender_var=StringVar()
gender_var.set("Male")

entry=Entry(window,font=("normal",18),textvariable=data_var).place(x=50,y=50)
radiobtn=Radiobutton(window,value="Male",variable=gender_var,text="Male").place(x=100,y=100)
radiobtn=Radiobutton(window,value="Female",variable=gender_var,text="Female").place(x=150,y=100)
btn=Button(window,text="click me",height=1,width=20,fg="red",bg="blue",command=clickme).place(x=150,y=150)

window.mainloop()
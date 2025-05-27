from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("New window")
window.geometry("600x600")


def clickme():
    data=data_var.get()
    print(data)
    msg=messagebox.showwarning("information",data)


data_var=StringVar()


entry=Entry(window,font=("normal",18),textvariable=data_var).place(x=50,y=50)

btn=Button(window,text="click me",height=1,width=20,fg="red",bg="blue",command=clickme).place(x=100,y=100)

window.mainloop()
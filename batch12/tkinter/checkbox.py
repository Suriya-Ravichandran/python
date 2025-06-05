from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("New window")
window.geometry("600x600")


def clickme():
    data=data_var.get()
    Checkbutton=Checkbutton1.get()
    print(data)
    print(Checkbutton)
    msg=messagebox.showwarning("information",data)


data_var=StringVar()
Checkbutton1=IntVar()

entry=Entry(window,font=("normal",18),textvariable=data_var).place(x=50,y=50)
Button1 = Checkbutton(window, text = "Tutorial", variable = Checkbutton1, onvalue = 1, offvalue = 0, height = 2, width = 10).place(x=100,y=100)
btn=Button(window,text="click me",height=1,width=20,fg="red",bg="blue",command=clickme).place(x=150,y=150)

window.mainloop()
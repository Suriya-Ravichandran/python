from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry("600x600")

def clickme():
    msg=msg_var.get()
    print(msg)
    messagebox.showinfo("Infromation",msg)
   


msg_var=StringVar()
textfield=Entry(window,font=("Normal",18),width=20,textvariable=msg_var).place(x=150,y=50)
btn=Button(window,text="click me",height=2,width=14,bg="blue",fg="white",command=clickme).place(x=225,y=100)


window.mainloop()
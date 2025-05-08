from tkinter import *
from tkinter.messagebox import *
window=Tk()
window.title("BUTTON WINDOW")
window.geometry("600x600")

# event

def showmsg():
    data=data_var.get()
    print(data)
    showinfo("Message",data)


data_var=StringVar()
data_var.set("Messsage Here")


textfield=Entry(window,textvariable=data_var,font=("Arial",18)).place(x=150,y=50)
btn=Button(window,text="click me",bg="black",fg="white",height=2,width=10,command=showmsg).place(x=250,y=100)
window.mainloop()
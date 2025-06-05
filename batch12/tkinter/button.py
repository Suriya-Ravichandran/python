from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry('600x600')
window.title("New Window")

def clickme():
    msg=messagebox.showinfo("Message","Hello world")



btn=Button(window,height=1,width=15,text="click me",background="blue",fg="white",command=clickme).place(x=150,y=50)


window.mainloop()
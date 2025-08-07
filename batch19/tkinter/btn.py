from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("600x600")
window.title("button show")

def clickme():
    messagebox.showinfo("Information","Hello wolrd")


btn=Button(window,text="clickme",height=1,width=12,bg="blue",fg="white",command=clickme).place(x=50,y=50)


window.mainloop()
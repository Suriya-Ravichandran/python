from tkinter import *
from tkinter import messagebox


window=Tk()
window.geometry("600x600")



def clickme():
    messagebox.showwarning("Information","wrong buton")
    messagebox.showinfo("Information","wrong buton")
    messagebox.showerror("Information","wrong buton")



btn=Button(window,text="Click me",height=2,width=15,bg="blue",fg="white",command=clickme).pack()

window.mainloop()
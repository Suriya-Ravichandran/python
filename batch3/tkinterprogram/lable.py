from tkinter import *

# window creation
window=Tk()
window.title("new window")

window.geometry("450x450")

# setlables
var=StringVar()
lable=Label( window,textvariable=var,relief=RAISED)
var.set("Hello this is Livewire")

lable.pack()

window.mainloop()


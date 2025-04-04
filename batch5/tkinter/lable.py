from tkinter import *


# All windows Here
window=Tk()
window.title("My First GUI")
window.geometry("400x400")
window.configure(bg="red")

# All widgets Here

label1=Label(window,text="HELLO WORLD",font=("bold",25),fg="White", bg="red")


# set postion for all widgets
label1.pack()


# program start here
window.mainloop()
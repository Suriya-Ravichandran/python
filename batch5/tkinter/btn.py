from tkinter import *
from tkinter import messagebox

# function all here

def hello():
    msg=messagebox.showinfo("Alert !","Hello world")








# All windows Here
window=Tk()
window.title("My First GUI")
window.geometry("400x400")
window.configure(bg="red")




# All widgets Here

btn_var=StringVar()
btn_var.set("Click me")

btn1=Button(window,textvariable=btn_var,bg="blue",fg="white",height=3,width=25,command=hello)




# set postion for all widgets
btn1.place(x=50,y=50)


# program start here
window.mainloop()
from tkinter import *


def hello():
    name=msg.get()
    print("your Message:",name)

# All windows Here
window=Tk()
window.title("My First GUI")
window.geometry("400x400")
window.configure(bg="red")

# All widgets Here
msg=StringVar()
textbox1=Entry(window,textvariable=msg,width=20,font=("normal",20))
btn1=Button(window,text="Submit",bg="blue",fg="white",height=3,width=25,command=hello)
# set postion for all widgets

textbox1.place(x=50,y=50)
btn1.place(x=50,y=110)

# program start here
window.mainloop()
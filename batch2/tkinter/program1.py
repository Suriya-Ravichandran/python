from tkinter import *

window=Tk()

window.title("1 window title")
window.geometry("400x400")

Text_msg=StringVar()
Text_msg.set("Hello World")

Label1=Label(window,textvariable=Text_msg,height=3,width=40,fg="red")
Label1.pack()

window.mainloop()

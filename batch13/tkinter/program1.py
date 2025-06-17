from tkinter import *

Window=Tk()
Window.geometry("600x600")
Window.config(bg="black")
label=Label(Window,text="Helloworld",font=("normal",18),fg="red",bg="yellow").place(x=50,y=50)

Window.mainloop()
from tkinter import *

window=Tk()
window.title("New Window")
window.geometry("400x400")
window.configure(background="yellow")

label1=Label(window,text="Hello World",fg="red",background="blue",font=("bold",50))
label1.place(x=30,y=50)

window.mainloop()
from tkinter import *

window=Tk()
window.title("New window")
window.geometry("600x600")

hello=Label(window,text="Hello world",font=("Arial",18),fg="#238de1").place(x=50,y=50)

window.mainloop()
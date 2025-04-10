from tkinter import *

window=Tk()
window.title("New Window")
window.geometry("400x400")

label1=Label(window,text="UserName",fg="red")
textfield1=Entry(window)

label1.place(x=20,y=50)
textfield1.place(x=20,y=70)

window.mainloop()

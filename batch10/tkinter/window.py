from tkinter import *

window=Tk()

window.title("My new GUI App")
window.geometry("600x600")
window.configure(bg="#3d3938")

msg=StringVar()


text=Label(window,textvariable=msg,fg="white",font=("Bold",18),bg="#3d3938")


text.grid(column=0,row=0)

window.mainloop()
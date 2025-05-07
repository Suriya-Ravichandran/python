from tkinter import *

window=Tk()

window.title("My first GUI")
window.geometry("600x600")
window.configure(bg="#22221f")



text=Label(window,text="Hello World",bg="#22221f",fg="Yellow",font=("Arial",18))
text.pack(pady=10)



window.mainloop()
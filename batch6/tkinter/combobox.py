from tkinter import *
from tkinter import ttk

window=Tk()
window.title("New Window")
window.geometry("400x400")

option=["option1","option2","option3"]

combo = ttk.Combobox(window, values=option, state="readonly") 
combo.current(0)
combo.place(x=30,y=50)

window.mainloop()
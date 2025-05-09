from tkinter import *
from tkinter import ttk
window=Tk()
window.title("BUTTON WINDOW")
window.geometry("600x600")


options=["option1","option2","option3"]

combo=ttk.Combobox(window,values=options,state="readonly")
combo.current(0)
combo.pack(pady=50)

window.mainloop()
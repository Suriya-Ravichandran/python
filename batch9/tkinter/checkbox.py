from tkinter import *

window=Tk()

window.title("My first GUI")
window.geometry("600x600")
window.configure(bg="#22221f")


hoobies_var=StringVar()

hoobies=Checkbutton(window,text="Circket",variable=hoobies_var,onvalue=1,offvalue=0).place(x=10,y=50)



window.mainloop()
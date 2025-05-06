


from tkinter import *

window=Tk()

window.title("My new GUI App")
window.geometry("600x600")

data_var=StringVar()
data_var.set("Male")

r1=Radiobutton(window,text="Male",variable=data_var,value="Male").pack(pady=20)
r2=Radiobutton(window,text="Female",variable=data_var,value="Female").pack(pady=40)

window.mainloop()


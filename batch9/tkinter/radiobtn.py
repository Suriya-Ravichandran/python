from tkinter import *
from tkinter.messagebox import *
window=Tk()
window.title("BUTTON WINDOW")
window.geometry("600x600")

# event

def submit():
    gender=gender1_var.get()
    print(gender)


gender1_var=StringVar()
gender1_var.set("Male")


male=Radiobutton(window,text="Male",font=("Arial",18),variable=gender1_var,value="Male",).place(x=50,y=50)
Female=Radiobutton(window,font=("Arial",18),text="Female",variable=gender1_var,value="Female",).place(x=50,y=90)

btn=Button(window,text="click me",bg="black",fg="white",height=2,width=10,command=submit).place(x=50,y=130)
window.mainloop()
from tkinter import *


window=Tk()
window.title("New Window")
window.geometry("400x400")


def submit():
    data=data_var.get()
    print(data)

data_var=StringVar()
r1=Checkbutton(window,text="Male",variable=data_var,onvalue="Male",offvalue=0)
r2=Radiobutton(window,text="Female",variable=data_var,value="Female")
btn1=Button(window,text="Click Me",fg="white",background="red",command=submit)

r1.place(x=30,y=50)
r2.place(x=30,y=70)
btn1.place(x=30,y=100)

window.mainloop()
from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry('600x600')
window.title("New Window")

def clickme():
    data=gender_var.get()
    print(data)
    msg=messagebox.showinfo("Message",data)

gender_var=StringVar()
gender_var.set("Male")
radio=Radiobutton(window,text="Male",value="Male",variable=gender_var).place(x=150,y=50)
radio=Radiobutton(window,text="Female",value="Female",variable=gender_var).place(x=150,y=100)
btn=Button(window,height=1,width=15,text="click me",background="blue",fg="white",command=clickme).place(x=150,y=150)


window.mainloop() 
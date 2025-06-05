from tkinter import *
from tkinter import messagebox
window=Tk()
window.geometry('600x600')
window.title("New Window")

def submit():
    data=data_var.get()
    print(data)
    msg=messagebox.showinfo("Message",data)

data_var=StringVar()
textfield=Entry(window,font=("normal",18),textvariable=data_var).place(x=150,y=50)
btn=Button(window,height=1,width=15,text="Submit",background="blue",fg="white",command=submit).place(x=150,y=100)


window.mainloop()
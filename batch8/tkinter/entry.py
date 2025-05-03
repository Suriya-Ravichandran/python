from tkinter import *

window=Tk()

window.title("Hello world")
window.geometry("400x400")

def print_data():
    data=var_name.get()
    print("Name:",data)


var_name=StringVar()

label=Label(window,text="Name",fg="red",font=("bold",15))
textbox=Entry(window,width=20,font=("normal",18),textvariable=var_name,fg="red")
btn=Button(window,text="click me",fg="white",bg="blue",height=3,width=20,command=print_data)


label.place(x=50,y=50)
textbox.place(x=50,y=80)
btn.place(x=50,y=120)
window.mainloop()
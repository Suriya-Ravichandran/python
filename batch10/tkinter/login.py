from tkinter import *
from tkinter import messagebox
# event

def login():
    username=user_var.get()
    password=password_var.get()
    verifyuser="foo"
    verifypassword="foo@123"
    if username==verifyuser:
        if password==verifypassword:
            msg=messagebox.showinfo("Success","Login Success")
            window.withdraw()
            window2.deiconify()
        else:
            msg=messagebox.showerror("Failed","Incorrect Password")

    else:
        msg=messagebox.showerror("Failed","User Not Found")




# main window
window=Tk()


# storage variable

user_var=StringVar()
password_var=StringVar()

window.title("My new GUI App")
window.geometry("600x600")

text=Label(window,text="Login Page",fg="red",font=("bold",18)).pack(pady=10)
label1=Label(window,text="UserName",fg="black",font=("bold",15)).place(x=100,y=90)
textfield1=Entry(window,font=("normal",15),textvariable=user_var).place(x=200,y=90)
label2=Label(window,text="Password",fg="black",font=("bold",15)).place(x=100,y=130)
textfield2=Entry(window,font=("normal",15),textvariable=password_var,show="*").place(x=200,y=130)
btn1=Button(window,text="Login", bg="blue", fg="white", height=2, width=25, command=login).pack(pady=120)

# dashboad window
window2 = Toplevel(window)
window2.title("Dashboard")
window2.geometry("600x600")

text2=Label(window2,text="Dashboard Page",fg="red",font=("bold",18)).pack(pady=10)
label2=Label(window2,textvariable=user_var,fg="black",font=("bold",15)).place(x=100,y=90)
window2.withdraw()

window.mainloop()
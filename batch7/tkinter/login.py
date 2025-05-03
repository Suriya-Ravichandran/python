from tkinter import *
from tkinter import messagebox

window=Tk()
window.geometry("400x400")
window.title("My Firstapp")

def login():
    user=username.get()
    passwd=password.get()
    vuser="suriya"
    vpasswd="suriya@123"
    if(user==vuser):
        if(passwd==vpasswd):
            msg=messagebox.showinfo("message","Login success")
        else:
             msg=messagebox.showinfo("message","Incorect password")
    else:
         msg=messagebox.showinfo("message","user not found")

            


username=StringVar()
password=StringVar()


lable1=Label(window,text="Login Page",fg="red",font=("bold",20))

lable2=Label(window,text="Username",fg="blue",font="bold")
text1=Entry(window,width=40,font=("normal",10),textvariable=username)
lable3=Label(window,text="Password",fg="blue",font="bold")
text2=Entry(window,width=40,font=("normal",10),show="*",textvariable=password)
btn=Button(window,text="Login",height=2,background="blue",fg="white",width=20,command=login)




lable1.place(x=120,y=30)
lable2.place(x=50,y=70)
text1.place(x=50,y=90)
lable3.place(x=50,y=120)
text2.place(x=50,y=140)
btn.place(x=120,y=190)
window.mainloop()
from tkinter import *
from tkinter import ttk

window=Tk()
window.geometry("600x600")
window.title("New window")

# all fuctions here
def submit():
    name=name_var.get()
    email=email_var.get()
    password=password_var.get()
    gender=gender_var.get()
    dance=dance_var.get()
    singing=singing_var.get()
    contry=contry_var.get()
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Password: {password}")
    print(f"Gender: {gender}")
    print(f"Hobby: [Dance: {dance},Singing: {singing}]")
    print(f"Contry: {contry}")


# data_vars here
name_var=StringVar()
email_var=StringVar()
password_var=StringVar()
gender_var=StringVar()
gender_var.set("Male")
dance_var=IntVar()
singing_var=IntVar()
contry_var=StringVar()

contry_value=[
    "india",
    "china",
    "Russia",
]

# all widgets here
# name
name_label=Label(window,text="Name",font=("bold",17)).place(x=50,y=50)
name=Entry(window,width=20,font=("arial",15),textvariable=name_var).place(x=50,y=80)

# email
email_label=Label(window,text="Email",font=("bold",17)).place(x=50,y=120)
email=Entry(window,width=20,font=("arial",15),textvariable=email_var).place(x=50,y=160)

# password

password_label=Label(window,text="Password",font=("bold",17)).place(x=50,y=190)
password=Entry(window,width=20,font=("arial",15),textvariable=password_var,show="*").place(x=50,y=230)

# gender
gender_label=Label(window,text="Gender",font=("bold",17)).place(x=50,y=260)
male=Radiobutton(window,text="Male",value="Male",variable=gender_var).place(x=50,y=290)
female=Radiobutton(window,text="Female",value="Female",variable=gender_var).place(x=130,y=290)

# hobby 
hobby_label=Label(window,text="Hobby",font=("bold",17)).place(x=50,y=320)
dance=Checkbutton(window,text="Dance",onvalue=1,offvalue=0,variable=dance_var).place(x=50,y=360)
singing=Checkbutton(window,text="Singing",onvalue=1,offvalue=0,variable=singing_var).place(x=150,y=360)


# contry
contry_label=Label(window,text="Contry",font=("bold",17)).place(x=50,y=400)
contry=ttk.Combobox(window,values=contry_value,textvariable=contry_var).place(x=50,y=440)

btn=Button(window,text="Submit",height=1,width=12,bg="blue",fg="white",command=submit).place(x=50,y=480)

window.mainloop()
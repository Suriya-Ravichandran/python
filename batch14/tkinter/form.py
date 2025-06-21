from tkinter import *
from tkinter import messagebox
from tkinter import ttk
window=Tk()
window.geometry("600x600")

# submit function
def submit():
    name=name_var.get()
    email=email_var.get()
    phoneno=phone_var.get()
    if len(phoneno)==10:
        phoneno=phoneno
    else:
        phoneno=None
        messagebox.showerror("Error","Invaild Phone number")
    gender=gender_var.get()
    hobbies=f"Dance: {dance_var.get()} Singing: {singing_var.get()}"
    contry=contry_var.get()



    if name==None or email==None or phoneno==None or gender==None:
        print("Data Not Submit")
    else: 
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Phone No: {phoneno}")
        print(f"Gender: {gender}")
        print(f"Hobbies: {hobbies}")
        print(f"Contry: {contry}")
   

# variables to store a data
name_var=StringVar()
email_var=StringVar()
phone_var=StringVar()
gender_var=StringVar()
gender_var.set("Male")
# hobbies var
dance_var=IntVar()
singing_var=IntVar()
# contrys

options=[
    "india",
    "USA",
    "Russia",
]
contry_var=StringVar()


# widgets

# name field
namelabel=Label(window,text="Name",font=("Arial",10),).place(x=50,y=50)
namefield=Entry(window,font=("Normal",18),width=20,textvariable=name_var).place(x=50,y=80)

# email
emaillabel=Label(window,text="Email",font=("Arial",10),).place(x=50,y=120)
emailfield=Entry(window,font=("Normal",18),width=20,textvariable=email_var).place(x=50,y=150)

# phone no

phonelabel=Label(window,text="Phone No",font=("Arial",10),).place(x=50,y=190)
phonefield=Entry(window,font=("Normal",18),width=20,textvariable=phone_var).place(x=50,y=220)

# genders
genderslabel=Label(window,text="Gender",font=("Arial",10),).place(x=50,y=260)
male=Radiobutton(window,text="Male",value="Male",variable=gender_var).place(x=50,y=290)
female=Radiobutton(window,text="Female",value="Female",variable=gender_var).place(x=100,y=290)

# Hobbies
Hobbieslabel=Label(window,text="Hobbies",font=("Arial",10),).place(x=50,y=320)
dance=Checkbutton(window,text="Dance",variable=dance_var,onvalue=1,offvalue=0).place(x=50,y=350)
singing=Checkbutton(window,text="Singing",variable=singing_var,onvalue=1,offvalue=0).place(x=130,y=350)

# contry
contrylabel=Label(window,text="Contry",font=("Arial",10),).place(x=50,y=390)
contry=ttk.Combobox(window,values=options,textvariable=contry_var).place(x=50,y=430)



btn=Button(window,text="Submit",height=2,width=14,bg="blue",fg="white",command=submit).place(x=50,y=470)

window.mainloop()
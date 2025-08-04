from tkinter import *
from tkinter import ttk
from tkinter import messagebox

window=Tk()
window.geometry("600x600")

# submission function
def submit():
    name=name_var.get()
    email=email_var.get()
    password=password_var.get()
    gender=gender_var.get()
    cricket=cricket_var.get()
    dance=dancing_var.get()
    singing=singing_var.get()
    other=other_var.get()
    contry=country_var.get()

    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"password: {password}")
    print(f"gender: {gender}")
    print(f"Hobbies: [cricket: {cricket},dancing: {dance},singing: {singing},other: {other}]")
    print(f"contry: {contry}")
    msg=messagebox.showinfo("Submission","Form submitted success")

 



# varibles
name_var=StringVar()
email_var=StringVar()
password_var=StringVar()
gender_var=StringVar()
gender_var.set("Male")
cricket_var=IntVar()
dancing_var=IntVar()
singing_var=IntVar()
other_var=IntVar()
country_var=StringVar()
countryopition=[
    "India",
    "Russia",
    "China",
]



# widgets

# heading
heading=Label(window,text="Student Registeration",font=("bold",18)).pack()
# name field
name=Label(window,text="Name",font=("bold",12)).place(x=50,y=50)
name_input=Entry(window,width=30,font=('Arial',13),textvariable=name_var).place(x=50,y=80)


# email field
email=Label(window,text="Email",font=("bold",12)).place(x=50,y=120)
email_input=Entry(window,width=30,font=('Arial',13),textvariable=email_var).place(x=50,y=150)


# email field
password=Label(window,text="Password",font=("bold",12)).place(x=50,y=180)
password_input=Entry(window,width=30,font=('Arial',13),textvariable=password_var,show="*").place(x=50,y=210)

# Gender field
gender=Label(window,text="Gender",font=("bold",12)).place(x=50,y=240)
male=Radiobutton(window,text="Male",value="Male",variable=gender_var).place(x=50,y=270)
female=Radiobutton(window,text="Female",value="Female",variable=gender_var).place(x=150,y=270)

# Hobby field
Hobby=Label(window,text="Hobby",font=("bold",12)).place(x=50,y=300)
cricket=Checkbutton(window,text="Cricket",onvalue=1,offvalue=0,variable=cricket_var).place(x=50,y=330)
dance=Checkbutton(window,text="Dancing",onvalue=1,offvalue=0,variable=dancing_var).place(x=140,y=330)
singing=Checkbutton(window,text="Singing",onvalue=1,offvalue=0,variable=singing_var).place(x=230,y=330)
other=Checkbutton(window,text="Other",onvalue=1,offvalue=0,variable=other_var).place(x=300,y=330)

# Hobby field
country=Label(window,text="Country",font=("bold",12)).place(x=50,y=360)
country_input=ttk.Combobox(window,values=countryopition,textvariable=country_var).place(x=50,y=400)


# submit btn
btn=Button(window,text="Submit",height=2,width=18,bg="blue",fg="white",command=submit).place(x=50,y=480)


window.mainloop()
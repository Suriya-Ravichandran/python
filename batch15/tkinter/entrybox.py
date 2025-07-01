from tkinter import *
from tkinter import messagebox
from tkinter import ttk
window=Tk()
window.geometry("600x600")


def clickme():
   name=name_var.get()
   email=email_var.get()
   gender=gender_var.get()
   movie_hobbies=hobies_movie.get()
   singing_hobbies=hobies_singing.get()
   contry=contry_var.get()
   print(f"Name: {name}")
   print(f"Email: {email}")
   print(f"Gender: {gender}")
   print(f"Hobbies: Movie {movie_hobbies},Singing {singing_hobbies}")
   print(f"Contry: {contry}")
  


name_var=StringVar()
email_var=StringVar()
gender_var=StringVar()
gender_var.set("Male")
hobies_movie=IntVar()
hobies_singing=IntVar()
contry_var=StringVar()
contryvalue=[
   "India",
   "USA",
   "Russia",
   "China"
]




name_label=Label(window,text="Enter Name ",font=("Arial",12),fg="Red").place(x=50,y=50)
name=Entry(window,textvariable=name_var,width=25,font=("arial",15)).place(x=50,y=90)
email_label=Label(window,text="Enter Email ",font=("Arial",12),fg="Red").place(x=50,y=130)
email=Entry(window,textvariable=email_var,width=25,font=("arial",15)).place(x=50,y=160)
gender_label=Label(window,text="Gender",font=("Arial",12),fg="Red").place(x=50,y=200)
gender_male=Radiobutton(window,variable=gender_var,text="Male",value="Male").place(x=50,y=240)
gender_female=Radiobutton(window,variable=gender_var,text="Female",value="Female").place(x=150,y=240)
hobbies_label=Label(window,text="Hobbies",font=("Arial",12),fg="Red").place(x=50,y=280)
movie_hobbies=Checkbutton(window,text="Movies",variable=hobies_movie,offvalue=0,onvalue=1).place(x=50,y=310)
singing_hobbies=Checkbutton(window,text="Singing",variable=hobies_singing,offvalue=0,onvalue=1).place(x=150,y=310)
contry_label=Label(window,text="Contry",font=("Arial",12),fg="Red").place(x=50,y=350)
contry=ttk.Combobox(window,textvariable=contry_var,values=contryvalue).place(x=50,y=400)


btn=Button(window,text="Click me",height=2,width=15,bg="blue",fg="white",command=clickme).place(x=50,y=440)

window.mainloop()

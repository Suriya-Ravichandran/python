from tkinter import *
from tkinter import messagebox
window=Tk()

window.title("Student Registeration Form")
window.geometry("600x700")
window.configure(bg="gray")


# submit function here
def submit():
    name_var=name.get()
    age_var=age.get()
    father_var=fathername.get()
    gender_var=gender.get()
    hobbies1_var=hobbies1.get()
    hobbies2_var=hobbies2.get()

    print("--------student data------------")
    print("Name:",name_var)
    print("Age:",age_var)
    print("Father name:",father_var)
    print("Gender:",gender_var)
    print("Hobbies:",hobbies1_var,hobbies2_var)

    msg=messagebox.showinfo("Success","Thank you for submit form")
#varable data
name=StringVar()
age=StringVar()
fathername=StringVar()


gender=StringVar()
gender.set("Male")

hobbies1=StringVar()
hobbies2=StringVar()



    


# elements class creation
Label1=Label(window,fg="White",font=("bold",25),text="Student Registration Form",bg="gray")
Label2=Label(window,fg="white",font=("bold",20),text="Name",bg="gray")
Textfield1=Entry(window,font=("normal",18),textvariable=name)
Label3=Label(window,fg="white",font=("bold",20),text="Age",bg="gray")
Textfield2=Entry(window,font=("normal",18),textvariable=age)
Label4=Label(window,fg="white",font=("bold",20),text="Father name",bg="gray")
Textfield3=Entry(window,font=("normal",18),textvariable=fathername)
Label5=Label(window,fg="white",font=("bold",20),text="Gender",bg="gray")
radio1=Radiobutton(window,text="Male",variable=gender,value="Male",bg="gray",fg="red",font=("bold",18))
radio2=Radiobutton(window,text="Female",variable=gender,value="Female",bg="gray",fg="red",font=("bold",18))
label6=Label(window,fg="white",font=("bold",20),text="Hobbies",bg="gray")
checkbox1=Checkbutton(window,text="cricket",variable=hobbies1,onvalue="cricket",bg="gray",fg="red",font=("bold",18),offvalue=0)
checkbox2=Checkbutton(window,text="Football",variable=hobbies2,onvalue="football",bg="gray",fg="red",font=("bold",18),offvalue=0)

btn=Button(window,text="Submit",fg="white",bg="blue",height=2,width=10,command=submit)


#place elements 

Label1.place(x=100,y=50)
Label2.place(x=50,y=100)
Textfield1.place(x=130,y=100)
Label3.place(x=50,y=140)
Textfield2.place(x=130,y=140)
Label4.place(x=50,y=180)
Textfield3.place(x=220,y=180)
Label5.place(x=50,y=230)
radio1.place(x=200,y=230)
radio2.place(x=280,y=230)
label6.place(x=50,y=265)
checkbox1.place(x=200,y=265)
checkbox2.place(x=300,y=265)
btn.place(x=50,y=310)
window.mainloop()
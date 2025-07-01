from tkinter import *
import qrcode
from PIL import Image,ImageTk


window=Tk()
window.geometry("600x600")

def genqr():
    data=data_var.get()
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    imgtk=ImageTk.PhotoImage(img)
    image_label.config(image=imgtk)
    image_label.image=imgtk




data_var=StringVar()


data_input=Entry(window,textvariable=data_var,width=25,font=("arial",15)).place(x=50,y=50)
btn=Button(window,text="Genrate QR",height=1,width=15,bg="blue",fg="white",command=genqr).place(x=350,y=50)
image_label=Label(window)
image_label.place(x=50,y=100)

window.mainloop()
from tkinter import *
from PIL import Image,ImageTk

import qrcode

window=Tk()
window.title("New window")
window.geometry("600x600")

def genrateqrcode():
    data=data_var.get()

    qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=(225, 70, 35), back_color=(210, 196, 60))
    img_tk = ImageTk.PhotoImage(img)
    image_lable.config(image=img_tk)
    image_lable.image=img_tk


data_var=StringVar()


entry=Entry(window,font=("normal",20),textvariable=data_var).place(x=50,y=50)
btn=Button(window,text="Genrate Qr",height=2,width=10,fg="white",bg="blue",command=genrateqrcode).place(x=320,y=50)
image_lable=Label(window)
image_lable.place(x=200,y=150)

window.mainloop()
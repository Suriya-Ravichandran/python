from tkinter import *
import qrcode
from PIL import Image,ImageTk


window=Tk()
window.geometry("600x600")

def gen_qr():
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
    img_tk=ImageTk.PhotoImage(img)
    image_lable.config(image=img_tk)
    image_lable.image=img_tk


data_var=StringVar()

label=Label(window,text="QRcode Genrator",font=("Arial",18)).place(x=225,y=50)
input=Entry(window,font=("Arial",20),width=25,textvariable=data_var).place(x=50,y=90)
btn=Button(window,text="Genrate Qr",height=2,width=14,bg="blue",fg="white",command=gen_qr).place(x=450,y=90)
image_lable=Label(window)
image_lable.place(x=50,y=130)

window.mainloop()
from tkinter import *
from PIL import Image,ImageTk
import qrcode

window=Tk()
window.title("QR Genrator")
window.geometry("600x600")

def genrateqr():
    data=qrdata.get()
     # Create the QR code
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)

    qr.add_data(data)
    qr.make(fit=True)
    # Create an image of the QR code
    img = qr.make_image(fill="black", back_color="white")

    img_tk = ImageTk.PhotoImage(img)

    # Create a label to display the image
    image_lable.config(image=img_tk)
    image_lable.image=img_tk
    

qrdata=StringVar()
textbox1=Entry(window,textvariable=qrdata,width=20,font=("normal",20))
btn1=Button(window,text="Submit",bg="blue",fg="white",height=2,width=18,command=genrateqr)
image_lable=Label(window)

textbox1.place(x=50,y=50)
btn1.place(x=360,y=50)
image_lable.place(x=50,y=100)
window.mainloop()


def genrateqr():
    data=qrdata.get()
     # Create the QR code
    qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4,)

    qr.add_data(data)
    qr.make(fit=True)
    # Create an image of the QR code
    img = qr.make_image(fill="black", back_color="white")

    img_tk = ImageTk.PhotoImage(img)

    # Create a label to display the image
    image_lable.config(image=img_tk)
    image_lable.image=img_tk
    

qrdata=StringVar()
textbox1=Entry(window,textvariable=qrdata,width=20,font=("normal",20))
btn1=Button(window,text="Submit",bg="blue",fg="white",height=2,width=18,command=genrateqr)
image_lable=Label(window)

textbox1.place(x=50,y=50)
btn1.place(x=360,y=50)
image_lable.place(x=50,y=100)
window.mainloop()
from tkinter import *
import qrcode
from PIL import Image,ImageTk
from tkinter import filedialog

window=Tk()
window.geometry("600x600")
window.title("New window")

img=None
def qrcodegen():
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
    image_lable.config(image=imgtk)
    image_lable.image=imgtk

     # download btn function
    def download_qr():
        if img:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png")],title="Save QR Code")
            if file_path:
                img.save(file_path)
    Button(window,text="Download QR", height=2, width=14, bg="green", fg="white", command=download_qr).place(x=400, y=140)


# data_var

data_var=StringVar()


# widgets
title=Label(window,text="QR CODE GENRATOR",font=("bold",17)).pack()
data=Entry(window,width=20,font=("arial",19),textvariable=data_var).place(x=50,y=80)

btn=Button(window,text="Genrate",height=1,width=19,bg="blue",fg="white",command=qrcodegen).place(x=50,y=120)

image_lable=Label(window)
image_lable.place(x=50,y=180)

window.mainloop()
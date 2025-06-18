from tkinter import *
import qrcode
from tkinter import filedialog
from PIL import Image,ImageTk
Window=Tk()
Window.geometry("600x600")

img=None
def genrateqr():
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
    
    # download btn function
    def download_qr():
        if img:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png")],title="Save QR Code")
            if file_path:
                img.save(file_path)
    Button(Window,text="Download QR", height=2, width=14, bg="green", fg="white", command=download_qr).place(x=480, y=140)

data_var=StringVar()

Title=Label(Window,text="QRcode Genrator",font=("Arial",20)).pack()
inputtitle=Label(Window,text="Type Url Here",font=("Arial",18)).place(x=50,y=50)
input=Entry(Window,width=24,font=("Arial",23),textvariable=data_var).place(x=50,y=80)
btn=Button(Window,text="Genrate QR",height=2,width=14,bg="blue",fg="white",command=genrateqr).place(x=480,y=80)
image_lable=Label(Window)
image_lable.place(x=50,y=120)
Window.mainloop()
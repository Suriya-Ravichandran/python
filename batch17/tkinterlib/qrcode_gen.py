from tkinter import *
import qrcode
from PIL import Image,ImageTk
from tkinter import filedialog
window=Tk()
window.geometry("600x600")

img=None
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
    imageqr.config(image=imgtk)
    imageqr.image=imgtk

    # download btn function
    def download_qr():
        if img:
            file_path = filedialog.asksaveasfilename(defaultextension=".png",filetypes=[("PNG files", "*.png")],title="Save QR Code")
            if file_path:
                img.save(file_path)
    Button(window,text="Download QR", height=2, width=14, bg="green", fg="white", command=download_qr).place(x=400, y=140)



# set a date
data_var=StringVar()

heading=Label(window,text="Qr code Genrator",font=("bold",18)).pack()
input1=Entry(window,width=20,font=('Arial',20),textvariable=data_var).place(x=50,y=50)
btn=Button(window,text="click me",height=2,width=18,bg="blue",fg="white",command=genqr).place(x=370,y=50)

imageqr=Label(window)
imageqr.place(x=50,y=150)

window.mainloop()
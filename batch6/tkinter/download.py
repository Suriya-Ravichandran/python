from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import qrcode

window = Tk()
window.title("QR Generator")
window.geometry("600x600")

qr_image = None  # Global variable to store the QR image (PIL Image object)

def generate_qr():
    global qr_image
    data = qrdata.get()
    if not data:
        return  # Do nothing if entry is empty

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(fill_color="black", back_color="white")
    img_tk = ImageTk.PhotoImage(qr_image)

    image_label.config(image=img_tk)
    image_label.image = img_tk

def download_qr():
    global qr_image
    if qr_image:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")],
                                                 title="Save QR Code")
        if file_path:
            qr_image.save(file_path)

qrdata = StringVar()

textbox1 = Entry(window, textvariable=qrdata, width=20, font=("normal", 20))
btn1 = Button(window, text="Generate", bg="blue", fg="white", height=2, width=18, command=generate_qr)
download_btn = Button(window, text="Download", bg="green", fg="white", height=2, width=18, command=download_qr)
image_label = Label(window)

textbox1.place(x=50, y=50)
btn1.place(x=360, y=50)
download_btn.place(x=360, y=110)
image_label.place(x=50, y=150)

window.mainloop()

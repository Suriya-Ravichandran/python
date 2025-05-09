from tkinter import *
from PIL import Image, ImageTk
import qrcode
from tkinter import filedialog

window = Tk()
window.title("QR Code Generator")
window.geometry("600x600")

qr_image = None  # Global variable to store the QR image

def genrateqr():
    global qr_image
    data = data_var.get()
    if not data:
        return

    # Create the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(data)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill="black", back_color="white")

    qr_image = img  # Save image globally for download

    img_tk = ImageTk.PhotoImage(img)

    # Display the image in the label
    image_label.config(image=img_tk)
    image_label.image = img_tk


def download_qr():
    global qr_image
    if qr_image is not None:
        file_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png")])
        if file_path:
            qr_image.save(file_path)


data_var = StringVar()
Entry(window, textvariable=data_var, font=("Arial", 18)).place(x=150, y=50)

Button(window, text="Generate QR", bg="black", fg="white", height=2, width=10,
       command=genrateqr).place(x=150, y=100)

Button(window, text="Download QR", bg="green", fg="white", height=2, width=10,
       command=download_qr).place(x=300, y=100)

image_label = Label(window)
image_label.place(x=200, y=170)

window.mainloop()

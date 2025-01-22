import tkinter as tk
from PIL import Image, ImageTk
import qrcode

# Create a Tkinter window
root = tk.Tk()
root.title("QR Code Generator")

# Set window size
root.geometry("300x300")

# Function to generate and display QR code
def generate_qr():
    # Get the input text (can replace this with any string you want to encode)
    data = "https://www.gocourse.in"
    
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

    # Convert the image to a Tkinter-compatible format
    img_tk = ImageTk.PhotoImage(img)

    # Create a label to display the image
    qr_label.config(image=img_tk)
    qr_label.image = img_tk

# Add a button to generate the QR code
btn_generate = tk.Button(root, text="Generate QR Code", command=generate_qr)
btn_generate.pack(pady=20)

# Label to hold the QR code image
qr_label = tk.Label(root)
qr_label.pack()

# Run the Tkinter event loop
root.mainloop()

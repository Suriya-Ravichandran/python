from tkinter import *
from PIL import Image, ImageTk


window=Tk()
window.title("Image")
window.geometry("600x600")

# create a image

# open
img=Image.open("cat.jpg")
# set a size
img_resized = img.resize((300, 300))
# genrate img
photo=ImageTk.PhotoImage(img_resized)


image_lable=Label(window,image=photo)
image_lable.pack()

image_lable.image=photo
window.mainloop()
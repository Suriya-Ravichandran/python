from tkinter import *

from tkinter import messagebox

# window creation 
window=Tk()
window.title("Button in tk")
window.geometry("450x450")

# event 
def btnclicked():
    msg=messagebox.showinfo("Alert","I am suriya")

btn=Button(window,text="click me",command=btnclicked)
# Set the initial position using .place() (x and y coordinates)
btn.place(x=200, y=100)
# Move the button to a new position
btn.place(x=50, y=160)  # You can update x and y to change the button's position

window.mainloop()


from tkinter import *

# Event functions
def clickedtonext():
    window1.withdraw()
    window2.deiconify()

def clickedtoback():
    window2.withdraw()
    window1.deiconify()

# Main window
window1 = Tk()
window1.title("Main Window")
window1.geometry("600x600")
window1.configure(bg="#3d3938")

btn1 = Button(window1, text="Next page", bg="blue", fg="white", height=2, width=25, command=clickedtonext)
btn1.pack(pady=20)

# Secondary window (starts hidden)
window2 = Toplevel(window1)
window2.title("Second Window")
window2.geometry("600x600")
window2.configure(bg="#3d3938")

btn2 = Button(window2, text="Back to Main", bg="blue", fg="white", height=2, width=25, command=clickedtoback)
btn2.pack(pady=20)

window2.withdraw()  # Hide second window initially

window1.mainloop()

import tkinter as tk

window=tk.Tk()
window.geometry("400x400")
window.title("My Firstapp")


lable1=tk.Label(window,text="Hello world",fg="red",bg="yellow")

lable1.place(x=50,y=30)

window.mainloop()
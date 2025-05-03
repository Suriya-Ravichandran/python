import tkinter as tk

def show_frame(frame):
    frame.tkraise()

root = tk.Tk()
root.title("Frame Switch Example")

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0, sticky='nsew')

tk.Label(frame1, text="This is Frame 1").pack()
tk.Button(frame1, text="Go to Frame 2", command=lambda: show_frame(frame2)).pack()

tk.Label(frame2, text="This is Frame 2").pack()
tk.Button(frame2, text="Back to Frame 1", command=lambda: show_frame(frame1)).pack()

show_frame(frame1)  # Start with frame1 visible
root.mainloop()

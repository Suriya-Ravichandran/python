import tkinter as tk

def hide_window():
    top.withdraw()

def close_window():
    top.destroy()

root = tk.Tk()
root.title("Main Window")

top = tk.Toplevel(root)
top.title("Popup")

tk.Button(top, text="Withdraw (Hide)", command=hide_window).pack(pady=10)
tk.Button(top, text="Destroy (Close)", command=close_window).pack(pady=10)

root.mainloop()

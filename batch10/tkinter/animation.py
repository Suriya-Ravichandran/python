import tkinter as tk

def animate_loading():
    global dot_count
    dots = '.' * (dot_count % 4)
    label.config(text=f"Loading{dots}")
    dot_count += 1
    root.after(500, animate_loading)

root = tk.Tk()
root.title("Loading Animation")
root.geometry("300x100")

dot_count = 0
label = tk.Label(root, text="Loading", font=("Arial", 20))
label.pack(pady=30)

animate_loading()

root.mainloop()

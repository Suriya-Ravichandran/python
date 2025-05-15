import tkinter as tk

class LoadingAnimation:
    def __init__(self, master):
        self.master = master
        self.label = tk.Label(master, text="Loading", font=("Helvetica", 20))
        self.label.pack(pady=20)
        self.chars = ["|", "/", "-", "\\"]
        self.index = 0
        self.animate()

    def animate(self):
        self.label.config(text="Loading " + self.chars[self.index])
        self.index = (self.index + 1) % len(self.chars)
        self.master.after(200, self.animate)

root = tk.Tk()
root.title("Loading Animation")
app = LoadingAnimation(root)
root.mainloop()

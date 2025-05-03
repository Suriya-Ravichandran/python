import tkinter as tk
from tkinter import messagebox

def new_file():
    messagebox.showinfo("New File", "New file created.")

def open_file():
    messagebox.showinfo("Open File", "File opened.")

def exit_app():
    root.quit()

def undo_action():
    messagebox.showinfo("Undo", "Undo last action.")

def about():
    messagebox.showinfo("About", "This is a simple Tkinter menu example.")

root = tk.Tk()
root.title("Tkinter Menu Example")

# Create menu bar
menubar = tk.Menu(root)

# File menu
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menubar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = tk.Menu(menubar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo_action)
menubar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=help_menu)

# Set the menu bar
root.config(menu=menubar)

root.mainloop()

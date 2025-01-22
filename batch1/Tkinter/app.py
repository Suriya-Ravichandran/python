from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo

# Create the main application window
root = Tk()
root.title("Untitled - Notepad")
root.geometry("620x420")

# Global variable to store the current file name
current_file = None

# Function to create a new file
def new_file():
    global current_file
    current_file = None
    text_area.delete(1.0, END)
    root.title("Untitled - Notepad")

# Function to open an existing file
def open_file():
    global current_file
    file_path = askopenfilename(
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        current_file = file_path
        with open(file_path, "r") as file:
            content = file.read()
        text_area.delete(1.0, END)
        text_area.insert(1.0, content)
        root.title(f"{file_path} - Notepad")

# Function to save the current file
def save_file():
    global current_file
    if current_file:
        with open(current_file, "w") as file:
            file.write(text_area.get(1.0, END))
        showinfo("Save", "File saved successfully.")
    else:
        save_as_file()

# Function to save the current file as a new file
def save_as_file():
    global current_file
    file_path = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Documents", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        current_file = file_path
        with open(file_path, "w") as file:
            file.write(text_area.get(1.0, END))
        root.title(f"{file_path} - Notepad")
        showinfo("Save As", "File saved successfully.")

# Function to exit the application
def exit_app():
    root.quit()

# Function to display about info
def about_notepad():
    showinfo("About Notepad", "This is a simple Notepad application built using Python and Tkinter.")

# Create a text area
text_area = Text(root, wrap="word", font=("Arial", 12))
text_area.pack(fill="both", expand=True, padx=5, pady=5)

# Add a scroll bar to the text area
scroll_bar = Scrollbar(text_area)
scroll_bar.pack(side="right", fill="y")
text_area.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=text_area.yview)

# Create the menu bar
menu_bar = Menu(root)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)
menu_bar.add_cascade(label="File", menu=file_menu)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Cut", command=lambda: root.focus_get().event_generate("<<Cut>>"))
edit_menu.add_command(label="Copy", command=lambda: root.focus_get().event_generate("<<Copy>>"))
edit_menu.add_command(label="Paste", command=lambda: root.focus_get().event_generate("<<Paste>>"))
edit_menu.add_command(label="Select All", command=lambda: text_area.tag_add(SEL, "1.0", END))
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About Notepad", command=about_notepad)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Configure the menu bar
root.config(menu=menu_bar)

# Start the application
root.mainloop()

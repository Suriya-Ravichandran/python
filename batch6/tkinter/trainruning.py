import tkinter as tk
from tkinter import ttk
import random

# Simulated train data
train_status = {
    "Train 101": "On Time",
    "Train 202": "Delayed",
    "Train 303": "On Time",
}

# Function to simulate updating train statuses
def update_status():
    for train in train_status:
        train_status[train] = random.choice(["On Time", "Delayed", "Cancelled"])
    refresh_table()
    root.after(3000, update_status)  # Update every 3 seconds

# Refresh the treeview with new data
def refresh_table():
    for i in tree.get_children():
        tree.delete(i)
    for train, status in train_status.items():
        tree.insert("", "end", values=(train, status))

# Tkinter setup
root = tk.Tk()
root.title("Live Train Status")
root.geometry("400x250")

# Treeview to display train data
columns = ("Train", "Status")
tree = ttk.Treeview(root, columns=columns, show="headings")
tree.heading("Train", text="Train")
tree.heading("Status", text="Status")
tree.pack(pady=20, fill=tk.BOTH, expand=True)

# Start live updates
update_status()

root.mainloop()

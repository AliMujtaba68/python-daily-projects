import tkinter as tk
from tkinter import messagebox, filedialog
import os

tasks = []
file_path = None

# Load tasks from a file
def load_tasks(path):
    global tasks
    if os.path.exists(path):
        with open(path, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    else:
        tasks = []
    update_listbox()

# Save tasks to a file
def save_tasks(path):
    with open(path, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# Add task
def add_task():
    task = entry.get().strip()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
        if file_path:
            save_tasks(file_path)

# Delete selected task
def delete_task():
    try:
        index = listbox.curselection()[0]
        removed = tasks.pop(index)
        update_listbox()
        if file_path:
            save_tasks(file_path)
    except IndexError:
        messagebox.showwarning("Warning", "Select a task to delete")

# Update listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Choose file to save/load
def choose_file():
    global file_path
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")],
        title="Select file to save tasks"
    )
    if path:
        file_path = path
        load_tasks(file_path)

# Main window
root = tk.Tk()
root.title("GUI To-Do List")
root.geometry("400x500")
root.resizable(False, False)

# Entry and Add button
entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", width=20, command=add_task)
add_btn.pack(pady=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=10)

# Delete button
del_btn = tk.Button(root, text="Delete Selected Task", width=25, command=delete_task)
del_btn.pack(pady=5)

# File select button
file_btn = tk.Button(root, text="Select File to Save/Load", width=25, command=choose_file)
file_btn.pack(pady=10)

root.mainloop()
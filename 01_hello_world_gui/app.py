# app.py
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Hello World GUI")
root.geometry("300x150")

# Add a label
label = tk.Label(root, text="Hello, World!", font=("Arial", 24))
label.pack(expand=True)

# Run the GUI loop
root.mainloop()
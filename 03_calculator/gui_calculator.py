import tkinter as tk

def click(value):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(value))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("GUI Calculator")
root.geometry("320x430")

# Display
entry = tk.Entry(root, width=16, font=("Arial", 24), borderwidth=5, justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Button layout
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

row = 1
col = 0

for button in buttons:

    if button == "=":
        action = calculate
    else:
        action = lambda x=button: click(x)

    tk.Button(root,
              text=button,
              width=5,
              height=2,
              font=("Arial",14),
              command=action).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col > 3:
        col = 0
        row += 1

# Clear button
tk.Button(root,
          text="C",
          width=22,
          height=2,
          font=("Arial",12),
          command=clear).grid(row=row, column=0, columnspan=4, pady=10)

root.mainloop()
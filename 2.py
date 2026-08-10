import tkinter as tk
from tkinter import messagebox

def hi():
    h='Hello'
    messagebox.showinfo("tirotir", f"welcome and {h}")
def bye():
    h='Good bye'
    messagebox.showinfo("tirotir", f"{h}")

root = tk.Tk()
root.title("KHoozestan")
root.geometry('300x200')
label = tk.Label(root, text="Hello!", bg="yellow", fg="red", font='18')
label.pack()

# Second label example
label = tk.Label(root, text="World!")
label.pack()

tk.Button(root, text="hi", command=hi).pack()
tk.Button(root, text="bye", command=bye).pack()

root.mainloop()
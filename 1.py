import tkinter as tk
from tkinter import messagebox

def hi():
    h='Hello'
    messagebox.showinfo("eror", f"welcome and {h}")
def bye():
    h='Good bye'
    messagebox.showinfo("eror", f"{h}")

root = tk.Tk()
root.title("mohamad")
root.geometry('300x200')
label = tk.Label(root, text="Hello!", bg="yellow", fg="red", font='18')
label.pack()

# Second label example
label = tk.Label(root, text="World!")
label.pack()

C:\Users\LAPCcenter\Desktop\p5\1.pytk.Button(root, text="bye", command=bye).pack()

root.mainloop()
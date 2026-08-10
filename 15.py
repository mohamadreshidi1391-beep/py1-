import tkinter as tk
from tkinter import messagebox

def jam():
    h='5+10=15'
    messagebox.showinfo("tirotir", f"welcome and {h}")
def tafrig():
    a='10-5=5'
    messagebox.showinfo("tirotir", f"{a}")

def taghsim():
    d='100/2=50'
    messagebox.showinfo("tirotir", f"{d}")







root = tk.Tk()
root.title("mohamad")
root.geometry('300x200')
label = tk.Label(root, text="Hello math!", bg="yellow", fg="red", font='18')
label.pack()

# Second label example
label = tk.Label(root, text="dragon!")
label.pack()

tk.Button(root, text="jam", command=jam).pack()
tk.Button(root, text="tafrig", command=tafrig).pack()

tk.Button(root, text="taghsim", command=taghsim).pack()


root.mainloop()








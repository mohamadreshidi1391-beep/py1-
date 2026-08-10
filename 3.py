import tkinter as tk
from tkinter import messagebox

def s():
    h='morning'
    messagebox.showinfo("tirotir", f"good {h}")
def z():
    a='.'
    messagebox.showinfo("tirotir", f"fter noon{a}")
def sh ():
    n='.'
    messagebox.showinfo("tirotir", f" good night{n}")

root = tk.Tk()
root.title("KHoozestan")
root.geometry('300x200')
label = tk.Label(root, text="Hello!", bg="purple", fg="green", font='18')
label.pack()

# Second label example
label = tk.Label(root, text="World!")
label.pack()

tk.Button(root, text="صبح بخیر", command=s).pack()
tk.Button(root, text="ظهر بخیر", command=z).pack()
tk.Button(root, text="شب بخیر ", command=sh).pack()


root.mainloop()
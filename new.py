import tkinter as tk

root = tk.Tk()
img = tk.PhotoImage(file="car.png")

tk.Label(root, text="Hello").pack(side="left")
tk.Label(root, image=img).pack(side="right")

root.mainloop()

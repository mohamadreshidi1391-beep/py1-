import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()

img = ImageTk.PhotoImage(Image.open("ccc.jpg").resize((80,80)))
tk.Label(root, text="Hello Tkinter").pack(side="left", padx=10)
tk.Label(root, image=img).pack(side="right", padx=10)

root.mainloop()

import tkinter as tk
def x():
    m=float(entry.get())


    label2.config(text=f'{m}\n  ')
root = tk.Tk()

root.title('izeh =mir')

root.geometry('300x200')

label = tk.Label(root, text='enter weight m')

label.pack()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text='convert', command=x)
button.pack()

label2 = tk.Label(root, text=  ' تبدیل به مسافت💕😊 '  )

label2.pack()

root.mainloop()
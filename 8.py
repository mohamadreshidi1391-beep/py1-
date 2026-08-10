import tkinter as tk
def x():
    toman=float(entry.get())
    toman=toman/159
    p=toman/245.710

    label2.config(text=f'{toman }dolar\n  {p}pounds')
root = tk.Tk()

root.title('izeh =mir')

root.geometry('300x200')

label = tk.Label(root, text='enter weight toman')

label.pack()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text='convert', command=x)
button.pack()

label2 = tk.Label(root, text=  '  تبدیل تومان به دلار 😁'  )

label2.pack()

root.mainloop()

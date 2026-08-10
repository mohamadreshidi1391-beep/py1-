import tkinter as tk
def x():
    dolar=float(entry.get())
    dolar=dolar*159
    p=dolar*1.3339

    label2.config(text=f'{dolar }toman\n  {p}pounds')
root = tk.Tk()

root.title('izeh')

root.geometry('300x200')

label = tk.Label(root, text='enter weight dolar')

label.pack()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text='convert', command=x)
button.pack()

label2 = tk.Label(root, text=' 😉تبدیل دلار به تومان😁')

label2.pack()

root.mainloop()

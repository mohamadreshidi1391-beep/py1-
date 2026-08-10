import tkinter as tk
def x():
    cm=float(entry.get())
    cm=cm/100
    p=cm*0.022

    label2.config(text=f'{cm }m\n  {p}pounds')
root = tk.Tk()

root.title('izeh =mir')

root.geometry('300x200')

label = tk.Label(root, text='enter weight cm')

label.pack()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text='convert', command=x)
button.pack()

label2 = tk.Label(root, text=  'تبدیل سانتی متر به متر 💕😊 '  )

label2.pack()

root.mainloop()



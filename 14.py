import tkinter as tk
def x():
    km=float(entry.get())
    km=km*0.621
    

    label2.config(text=f'{km}km\n  ')
root = tk.Tk()

root.title('izeh =mir')

root.geometry('300x200')

label = tk.Label(root, text='enter weight km')

label.pack()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text='convert', command=x)
button.pack()

label2 = tk.Label(root, text=  'تبدیل کیلومتر به مایل💕😊 '  )

label2.pack()

root.mainloop()
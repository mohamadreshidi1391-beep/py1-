import tkinter as tk
def x():
    mayl=float(entry.get())
    mayl=mayl*1.61
    

    label2.config(text=f'{mayl}km\n  ')
root = tk.Tk()

root.title('izeh =mir')

root.geometry('300x200')

label = tk.Label(root, text='enter weight mayl')

label.pack()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text='convert', command=x)
button.pack()

label2 = tk.Label(root, text=  'تبدیل مایل به کیلومتر 💕😊 '  )

label2.pack()

root.mainloop()
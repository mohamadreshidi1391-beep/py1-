import tkinter as tk
def x():
    cg=float(entry.get())
    f=cg*5.9
    

    label2.config(text=f'{f } cg\n  ')
root = tk.Tk()

root.title('izeh =mir')

root.geometry('300x200')

label = tk.Label(root, text='enter weight f')

label.pack()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text='convert', command=x)
button.pack()

label2 = tk.Label(root, text=  'تبدیل فارنهایت به سانتی گراد😊 😁'  )

label2.pack()

root.mainloop()
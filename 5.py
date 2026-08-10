import tkinter as tk

def x():
    cm=float(entry.get())
    inch=2.54*cm
    p=cm*0.0625

    label2.config(text=f'{inch } cm\n  {p}pounds')
root = tk.Tk()

root.title('izeh')

root.geometry('300x200')

label = tk.Label(root, text='enter weight inch')

label.pack()

entry = tk.Entry(root)

entry.pack()

button = tk.Button(root, text='convert', command=x)
button.pack()

label2 = tk.Label(root, text=' 👌تبدیل سانتی متر به اینچ را حتما امتحان کنید')

label2.pack()

root.mainloop()

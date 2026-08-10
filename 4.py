import tkinter as tk

def x():
    kg=float(entry.get())
    g=kg/1000
    p=g/0.22234435
    label2.config(text=f'{g}kg \n  {p}pounds')



root = tk.Tk()
root.title('Title')
root.geometry('300x200')
label = tk.Label(root, text='enter weight gram')
label.pack()
entry = tk.Entry(root)
entry.pack()
button = tk.Button(root, text='convert', command=x)
button.pack()
label2 = tk.Label(root, text='  !تبدیل گرم به کیلو گرم حتما امتحان کنید')
label2.pack()






root.mainloop()
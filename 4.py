import tkinter as tk
root = tk.Tk()
root.title('mr')
root.geometry('300x200')
label = tk.Label(root, text='Hello, baby!❤️')
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root,text= "ok", command=None)
button.pack()





root.mainloop()
import tkinter as tk
root = tk.Tk()
root.title('Title')
root.geometry('300x200')

entry = tk.Entry(root)
entry.pack()

entry2= tk.Entry(root)
entry2.pack()

button = tk.Button(root, text='Click Me', command=None)
button.pack()

label = tk.Label(root, text='Hello, World!')
label.pack()

root.mainloop()
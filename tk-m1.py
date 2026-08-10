import tkinter as tk
root = tk.Tk()
root.title('Title')
root.geometry('300x200')


menu = tk.Menu(root)
root.config(menu=menu)
file_menu = tk.Menu(menu)
menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New', command=None)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.quit)

root.mainloop()
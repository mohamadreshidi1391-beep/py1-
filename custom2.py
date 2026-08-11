import customtkinter
from tkinter import messagebox
root = customtkinter.CTk()
root.title('Inch to CM Calculator')
root.geometry('400x200')
    
entry = customtkinter.CTkEntry(root, width=70)
entry.pack()
    
button = customtkinter.CTkButton(root, text='Calculate', command=lambda: calculate_cm(entry.get()))
button.pack()
    
output_label = customtkinter.CTkLabel(root, text='')
output_label.pack()
    
def calculate_cm(inch_str):
    try:
        inch = float(inch_str)
        cm = inch * 2.54
        output_label.configure(text=f'Inch to CM Calculator inch = {cm:.2f} cm')
    except ValueError:
        messagebox.showerror('Error', 'Invalid input')
    
root.mainloop()
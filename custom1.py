import customtkinter
root = customtkinter.CTk()
root.title('Simple Window')
root.geometry('300x200')
    
label = customtkinter.CTkLabel(root, text='Hello, World!')
label.pack()
    
root.mainloop()
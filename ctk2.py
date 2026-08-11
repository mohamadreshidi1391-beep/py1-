import customtkinter as ctk

root = ctk.CTk()
root.title("Grid Layout")
root.geometry("300x200")

# Create widgets
label1 = ctk.CTkLabel(root, text="Name:")
label2 = ctk.CTkLabel(root, text="Email:")

entry1 = ctk.CTkEntry(root)
entry2 = ctk.CTkEntry(root)

button = ctk.CTkButton(root, text="Submit")

# Grid layout
label1.grid(row=0, column=0, padx=10, pady=10)
entry1.grid(row=0, column=1, padx=10, pady=10)
label2.grid(row=1, column=0, padx=10, pady=10)
entry2.grid(row=1, column=1, padx=10, pady=10)
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()

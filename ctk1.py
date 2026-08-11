import customtkinter as ctk

# Create main window
app = ctk.CTk()
app.title("My Custom App")
app.geometry("400x300")

# Add a label
label = ctk.CTkLabel(app, text="Hello World!")
label.pack(pady=20)

# Add a button
button = ctk.CTkButton(app, text="Click Me!")
button.pack(pady=10)

app.mainloop()

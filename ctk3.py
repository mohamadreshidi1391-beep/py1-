import customtkinter as ctk

# Set appearance mode and color theme
ctk.set_appearance_mode("dark")  # "light" or "dark"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

app = ctk.CTk()
app.title("Theme Example")
app.geometry("300x250")

# Different themed widgets
title = ctk.CTkLabel(app, text="Themed App", font=("Arial", 20))
title.pack(pady=20)

button1 = ctk.CTkButton(app, text="Blue Button")
button1.pack(pady=5)

button2 = ctk.CTkButton(app, text="Green Button", fg_color="green")
button2.pack(pady=5)

switch = ctk.CTkSwitch(app, text="Toggle Switch")
switch.pack(pady=10)

slider = ctk.CTkSlider(app, from_=0, to=100)
slider.pack(pady=10)

app.mainloop()

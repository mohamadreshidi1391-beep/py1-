import tkinter as tk
from PIL import Image, ImageTk

def calculate_sum():
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        result_label.config(text=f"Sum = {a + b}")
    except ValueError:
        result_label.config(text="Please enter numbers")

# ---------- main window ----------
root = tk.Tk()
root.title("Simple Sum Calculator")
root.geometry("420x200")

# ---------- main frame ----------
main_frame = tk.Frame(root)
main_frame.pack(padx=10, pady=10)

# ---------- left side (calculator) ----------
calc_frame = tk.Frame(main_frame)
calc_frame.grid(row=0, column=0, padx=10)

tk.Label(calc_frame, text="Number 1:").grid(row=0, column=0, sticky="w")
entry1 = tk.Entry(calc_frame, width=15)
entry1.grid(row=0, column=1)

tk.Label(calc_frame, text="Number 2:").grid(row=1, column=0, sticky="w")
entry2 = tk.Entry(calc_frame, width=15)
entry2.grid(row=1, column=1)

tk.Button(calc_frame, text="Calculate", command=calculate_sum)\
    .grid(row=2, column=0, columnspan=2, pady=5)

result_label = tk.Label(calc_frame, text="Sum = ")
result_label.grid(row=3, column=0, columnspan=2)

# ---------- right side (logo) ----------
logo_frame = tk.Frame(main_frame)
logo_frame.grid(row=0, column=1, padx=10)

img = Image.open("car.png")
img = img.resize((100, 100))
logo = ImageTk.PhotoImage(img)

logo_label = tk.Label(logo_frame, image=logo)
logo_label.image = logo  # keep reference
logo_label.pack()

# ---------- run ----------
root.mainloop()

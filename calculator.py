import tkinter as tk

# Function to update text on screen
def click(event):
    entry.delete(0, 'end')
    entry.insert(0, str(event))
    
# Function to calculate result when '=' button is pressed
def calculate():
    try:
        total = str(eval(entry.get()))
        if '.' in total and len(total) > 10 or (not '.' in total and len(total) > 7):
            entry.delete(0, 'end')
            entry.insert(0, "Number too big")
        else:
            entry.delete(0, 'end')
            entry.insert(0, total)
    except Exception as e:
        print(e)

# Function to clear the calculator
def clear():
    entry.delete(0, tk.END)

# Main program
root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Row 1 (Numbers and Operations)
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: click(9))

button_add = tk.Button(root, text="+", padx=39, pady=20)
button_subtract = tk.Button(root, text="-", padx=41, pady=20)
button_multiply = tk.Button(root, text="*", padx=40, pady=20)
button_divide = tk.Button(root, text="/", padx=41, pady=20)

# Row 2 (Numbers and Operations)
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: click(6))

button_multiply2 = tk.Button(root, text="*", padx=40, pady=20)
button_divide2 = tk.Button(root, text="/", padx=41, pady=20)

# Row 3 (Numbers and Operations)
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: click(3))

button_subtract2 = tk.Button(root, text="-", padx=41, pady=20)
button_add2 = tk.Button(root, text="+", padx=39, pady=20)

# Row 4 (Numbers and Operations)
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: click(0))
button_clear = tk.Button(root, text="Clear", padx=79, pady=20, command=clear)
button_equals = tk.Button(root, text="=", padx=91, pady=20, command=calculate)

# Positioning the buttons on screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_add.grid(row=1, column=3)
button_subtract.grid(row=2, column=3)
button_multiply.grid(row=3, column=3)
button_divide.grid(row=4, column=3)

# Row 2
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_multiply2.grid(row=2, column=3)
button_divide2.grid(row=3, column=3)

# Row 3
button_1.grid(row=4, column=0)
button_2.grid(row=4, column=1)
button_3.grid(row=4, column=2)

button_subtract2.grid(row=5, column=0)
button_add2.grid(row=5, column=1)

# Row 4
button_0.grid(row=5, column=2)
button_clear.grid(row=6, column=0, columnspan=3)
button_equals.grid(row=6, column=3)

root.mainloop()
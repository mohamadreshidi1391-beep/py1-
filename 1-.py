#izehkggtk
# kg_to_units_tkinter.py

import tkinter as tk
from tkinter import messagebox

def convert_kg_to_units(kg):
    grams = kg * 1000  # grams = kg * 1000
    pounds = kg * 2.20462  # pounds = kg * 2.20462
    return grams, pounds

def calculate_conversion():
    try:
        kg = float(entry_kg.get())
        grams, pounds = convert_kg_to_units(kg)
        result_label.config(text=f'{kg} kg is equal to {grams} grams.\n{kg} kg is equal to {pounds:.2f} pounds.')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter a valid number.')

# Create the main window
root = tk.Tk()
root.title('Kg to Grams and Pounds Converter')

# Create and place widgets
tk.Label(root, text='Enter weight in kilograms:').pack(pady=10)
entry_kg = tk.Entry(root)
entry_kg.pack(pady=5)

convert_button = tk.Button(root, text='Convert', command=calculate_conversion)
convert_button.pack(pady=10)

result_label = tk.Label(root, text='')
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

# Exercise 1: Modify the function to also return the weight in ounces.
# Formula: ounces = kg * 35.274
# Guidelines:
# 1. Add the conversion for ounces in the function.
""" def convert_kg_to_units(kg):
    grams = kg * 1000
    pounds = kg * 2.20462
    ounces = kg * 35.274
    return grams, pounds, ounces """

# Question 1: How do you add another unit conversion to the function?
# Answer: You add another unit conversion by including the conversion formula in the function and returning the new value.

# Exercise 2: Add a button to reset the input field and result label.
# Guidelines:
# 1. Create a new button and define a function to clear the input and result.
""" def reset_fields():
    entry_kg.delete(0, tk.END)
    result_label.config(text='')

reset_button = tk.Button(root, text='Reset', command=reset_fields)
reset_button.pack(pady=10) """

# Question 2: How do you clear the input field and result label in Tkinter?
# Answer: You clear the input field using the delete() method and reset the label using the config() method.

# Exercise 3: Write a function to convert Celsius to Fahrenheit and display the result in a new label.
# Formula: Fahrenheit = (Celsius * 9/5) + 32
# Guidelines:
# 1. Define a function for the conversion and create a new label to display the result.
""" def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def calculate_celsius_to_fahrenheit():
    try:
        celsius = float(entry_celsius.get())
        fahrenheit = celsius_to_fahrenheit(celsius)
        result_label_fahrenheit.config(text=f'{celsius}°C is equal to {fahrenheit:.2f}°F')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter a valid number.')

tk.Label(root, text='Enter temperature in Celsius:').pack(pady=10)
entry_celsius = tk.Entry(root)
entry_celsius.pack(pady=5)

convert_button_fahrenheit = tk.Button(root, text='Convert to Fahrenheit', command=calculate_celsius_to_fahrenheit)
convert_button_fahrenheit.pack(pady=10)

result_label_fahrenheit = tk.Label(root, text='')
result_label_fahrenheit.pack(pady=10) """

# Question 3: How do you create and display a new label in Tkinter?
# Answer: You create a new label using tk.Label() and display it using the pack() method.

# Exercise 4: Add error handling to check if the input is a negative number and display an appropriate message.
# Guidelines:
# 1. Use an if statement to check if the input is negative.
""" def calculate_conversion():
    try:
        kg = float(entry_kg.get())
        if kg < 0:
            messagebox.showerror('Input Error', 'Please enter a non-negative number.')
        else:
            grams, pounds = convert_kg_to_units(kg)
            result_label.config(text=f'{kg} kg is equal to {grams} grams.\n{kg} kg is equal to {pounds:.2f} pounds.')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter a valid number.') """

# Question 4: How do you handle invalid input values in Tkinter?
# Answer: You handle invalid input values using try-except blocks and additional checks like if statements.

# Exercise 5: Write a function to add two numbers entered in separate input fields and display the result.
# Formula: sum = a + b
# Guidelines:
# 1. Define a function to retrieve values from two input fields and display the sum.
""" def add_numbers():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        result_label_sum.config(text=f'Sum: {result}')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter valid numbers.')

tk.Label(root, text='Enter first number:').pack(pady=10)
entry_num1 = tk.Entry(root)
entry_num1.pack(pady=5)

tk.Label(root, text='Enter second number:').pack(pady=10)
entry_num2 = tk.Entry(root)
entry_num2.pack(pady=5)

add_button = tk.Button(root, text='Add', command=add_numbers)
add_button.pack(pady=10)

result_label_sum = tk.Label(root, text='')
result_label_sum.pack(pady=10) """

# Question 5: How do you retrieve and use values from multiple input fields in Tkinter?
# Answer: You retrieve values using the get() method and use them in your calculations or logic.

# Exercise 6: Write a function to calculate the average of three numbers entered in separate input fields.
# Formula: average = (a + b + c) / 3
# Guidelines:
# 1. Define a function to retrieve values from three input fields and calculate the average.
""" def calculate_average():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        num3 = float(entry_num3.get())
        average = (num1 + num2 + num3) / 3
        result_label_average.config(text=f'Average: {average:.2f}')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter valid numbers.')

tk.Label(root, text='Enter third number:').pack(pady=10)
entry_num3 = tk.Entry(root)
entry_num3.pack(pady=5)

average_button = tk.Button(root, text='Calculate Average', command=calculate_average)
average_button.pack(pady=10)

result_label_average = tk.Label(root, text='')
result_label_average.pack(pady=10) """

# Question 6: How do you calculate the average of three numbers in Python?
# Answer: You calculate the average by summing the three numbers and dividing by 3.

# Exercise 7: Write a function to convert USD to Pounds and display the result.
# Formula: Pounds = USD * conversion_rate (use a sample conversion rate, e.g., 0.73)
# Guidelines:
# 1. Define a function to convert USD to Pounds and display the result.
""" def usd_to_pounds(usd, conversion_rate=0.73):
    return usd * conversion_rate

def calculate_usd_to_pounds():
    try:
        usd = float(entry_usd.get())
        pounds = usd_to_pounds(usd)
        result_label_pounds.config(text=f'{usd} USD is equal to {pounds:.2f} Pounds')
    except ValueError:
        messagebox.showerror('Input Error', 'Please enter a valid number.')

tk.Label(root, text='Enter amount in USD:').pack(pady=10)
entry_usd = tk.Entry(root)
entry_usd.pack(pady=5)

convert_button_pounds = tk.Button(root, text='Convert to Pounds', command=calculate_usd_to_pounds)
convert_button_pounds.pack(pady=10)

result_label_pounds = tk.Label(root, text='')
result_label_pounds.pack(pady=10) """



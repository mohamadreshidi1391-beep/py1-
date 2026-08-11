#izehfuncdef
# Simple Function Definition
def greet(name):
    return f'Hello, {name}'

print(greet('World'))

# Exercise 1: Modify the function to greet with "Hi" instead of "Hello".
# Guidelines:
# 1. Change the string inside the return statement to "Hi".
""" def greet(name):
    return f'Hi, {name}'

print(greet('World')) """

# Question 1: How do you change the return value of a function in Python?
# Answer: You change the return value by modifying the expression inside the return statement.

# Exercise 2: Add a parameter to the function to include a greeting message (e.g., "Good morning").
# Guidelines:
# 1. Add a new parameter for the greeting message.
# 2. Use the new parameter in the return statement.
""" def greet(greeting, name):
    return f'{greeting}, {name}'

print(greet('Good morning', 'World')) """

# Question 2: How do you add multiple parameters to a function in Python?
# Answer: You add multiple parameters by listing them inside the parentheses, separated by commas.

# Exercise 3: Write a function that takes a name and age, and returns a greeting that includes both.
# Guidelines:
# 1. Add a new parameter for age.
# 2. Include both name and age in the return statement.
""" def greet(name, age):
    return f'Hello, {name}. You are {age} years old.'

print(greet('World', 30)) """

# Question 3: How do you include multiple variables in a return statement?
# Answer: You include multiple variables by using string formatting or concatenation in the return statement.

# Exercise 4: Modify the function to return the greeting in uppercase.
# Guidelines:
# 1. Use the upper() method to convert the string to uppercase before returning it.
""" def greet(name):
    return f'Hello, {name}'.upper()

print(greet('World')) """

# Question 4: How do you convert a string to uppercase in Python?
# Answer: You convert a string to uppercase using the upper() method.

# Exercise 5: Write a function that prints the greeting instead of returning it.
# Guidelines:
# 1. Use the print() function inside the function instead of return.
""" def greet(name):
    print(f'Hello, {name}')
    print("hello",name)

greet('World') """

# Question 5: What is the difference between returning a value and printing it in a function?
# Answer: Returning a value sends the result back to the caller, while printing a value displays it to the console.

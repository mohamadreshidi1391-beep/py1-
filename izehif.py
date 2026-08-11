#izehif
# If Statement Example
x = 10
if x > 5:
    print('x is greater than 5')
else:
    print('x is 5 or less')

# Exercise 1: Modify the code to check if x is greater than 10.
# Guidelines:
# 1. Change the condition in the if statement to x > 10.
""" x = 10
if x > 10:
    print('x is greater than 10')
else:
    print('x is 10 or less') """

# Question 1: How do you change the condition in an if statement?
# Answer: You change the condition by modifying the expression inside the if statement.

# Exercise 2: Add an elif statement to check if x is exactly 5.
# Guidelines:
# 1. Add an elif statement between the if and else statements.
""" x = 10
if x > 10:
    print('x is greater than 10')
elif x == 5:
    print('x is exactly 5')
else:
    print('x is less than or equal to 10 and not 5') """

# Question 2: What is the purpose of the elif statement in Python?
# Answer: The elif statement allows you to check multiple conditions in an if-else structure.

# Exercise 3: Change the value of x to 3 and observe the output.
# Guidelines:
# 1. Change the value of x to 3 and run the code.
""" x = 3
if x > 10:
    print('x is greater than 10')
elif x == 5:
    print('x is exactly 5')
else:
    print('x is less than or equal to 10 and not 5') """

# Question 3: How does the if-else structure handle different values of x?
# Answer: The if-else structure evaluates the conditions in order and executes the corresponding block of code for the first true condition.

# Exercise 4: Write a function that takes a number as an argument and prints whether it is positive, negative, or zero.
# Guidelines:
# 1. Define a function with a parameter for the number.
# 2. Use if-elif-else statements to check the number's value.
""" def check_number(num):
    if num > 0:
        print('The number is positive')
    elif num < 0:
        print('The number is negative')
    else:
        print('The number is zero')

check_number(10)
check_number(-5)
check_number(0) """

# Question 4: How do you use if-elif-else statements to handle multiple conditions?
# Answer: You use if-elif-else statements to evaluate multiple conditions in sequence, executing the block of code for the first true condition.

# Exercise 5: Modify the code to print a different message if x is less than 0.
# Guidelines:
# 1. Add an elif statement to check if x is less than 0.
""" x = -1
if x > 10:
    print('x is greater than 10')
elif x == 5:
    print('x is exactly 5')
elif x < 0:
    print('x is less than 0')
else:
    print('x is between 0 and 10 and not 5') """

# Question 5: How do you add additional conditions to an if-else structure?
# Answer: You add additional conditions by using elif statements between the if and else statements.

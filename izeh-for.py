#izehfor
# For Loop Example

# for i in range(5):
#     print(i)

# Exercise 1: Modify the code to print numbers from 1 to 5 instead of 0 to 4.
# Guidelines:
# 1. Adjust the range to start from 1 and end at 6.
""" for i in range(1, 6):
    print(i) """

# Question 1: How do you adjust the range to start from 1?
# Answer: You adjust the range by setting the start parameter to 1 in the range() function.

# Exercise 2: Print only the even numbers from 10 to 100.
# Guidelines:
# 1. Use a range that starts at 10 and ends at 101.
# 2. Use a step of 2 to get only even numbers.
""" for i in range(10, 101, 2):
    print(i) """

# Question 2: How can you check if a number is even in Python?
# Answer: You can check if a number is even by using the modulo operator (%) to see if the remainder is 0 when divided by 2.

# Exercise 3: Print the numbers in reverse order, from 4 to 0.
# Guidelines:
# 1. Use the range() function with a start of 4, end of -1, and step of -1.
""" for i in range(4, -1, -1):
    print(i) """

# Question 3: How do you reverse the order of a range in Python?
# Answer: You reverse the order of a range by setting a negative step value in the range() function.

# Exercise 4: Print the square of each number from 0 to 4.
# Guidelines:
# 1. Use the ** operator to calculate the square of each number.
""" for i in range(5):
    print(i ** 2) """

# Question 4: How do you calculate the square of a number in Python?
# Answer: You calculate the square of a number using the ** operator or the pow() function.

# Exercise 5: Skip the number 2 and print the rest.
# Guidelines:
# 1. Use an if statement to check if the number is 2 and use the continue statement to skip it.
""" for i in range(5):
    if i == 2:
        continue
    print(i) """

# Question 5: How can you skip an iteration in a for loop?
# Answer: You can skip an iteration in a for loop using the continue statement.

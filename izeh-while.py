#izehwhile
# While Loop Example

count = 0
while count < 5:
    print(count)
    count += 1


# Questions:
# 1. What will be the output of the original code?
# 2. How can you modify the loop to count down from 5 to 0?
# 3. What happens if you forget to increment the count variable inside the loop?
    
# Exercise 1:
# Modify the above code to print only even numbers between 0 and 10.

# Guidelines:
# 1. Use the modulo operator to check if a number is even.
# 2. Adjust the loop condition to stop at 10.
# 3. Ensure the count variable is incremented correctly to avoid an infinite loop.
'''
count = 0
while count <= 10:
    if count % 2 == 0:
        print(count)
    count += 1
'''
# Exercise 2:
# Modify the code to print numbers from 5 to 0 in descending order.

# Guidelines:
# 1. Initialize count to 5.
# 2. Change the loop condition to count down to 0.
# 3. Decrement the count variable inside the loop.
'''
count = 5
while count >= 0:
    print(count)
    count -= 1
'''
# Exercise 3:
# Modify the code to print the first 10 multiples of 3.

# Guidelines:
# 1. Initialize count to 0.
# 2. Adjust the loop condition to stop at 30.
# 3. Increment count by 3 inside the loop.
'''
count = 0
while count < 30:
    print(count)
    count += 3
'''
# Exercise 4:
# Modify the code to print the sum of numbers from 1 to 10.

# Guidelines:
# 1. Initialize count to 1 and sum to 0.
# 2. Adjust the loop condition to stop at 10.
# 3. Add count to sum inside the loop and increment count.
'''
count = 1
total_sum = 0
while count <= 10:
    total_sum += count
    count += 1
print(total_sum)
'''
# Exercise 5:
# Modify the code to print the factorial of a number (e.g., 5!).

# Guidelines:
# 1. Initialize count to 1 and factorial to 1.
# 2. Adjust the loop condition to stop at the desired number.
# 3. Multiply factorial by count inside the loop and increment count.
'''
count = 1
factorial = 1
number = 5  # You can change this to any number you want the factorial of
while count <= number:
    factorial *= count
    count += 1
print(factorial)
'''
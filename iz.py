#izehcolorama
from colorama import Fore, Style
print(Fore.RED + 'This is red text' + Style.RESET_ALL)

# Exercise 1: Modify the code to print text in blue instead of red.
# Guidelines:
# 1. Change Fore.RED to Fore.BLUE.
""" print(Fore.BLUE + 'This is blue text' + Style.RESET_ALL) """

# Question 1: How do you change the color of the text using the colorama library?
# Answer: You change the color of the text by using the Fore.COLOR_NAME attribute from the colorama library.

# Exercise 2: Print "This is red text" in bold red.
# Guidelines:
# 1. Use Style.BRIGHT to make the text bold.
""" print(Style.BRIGHT + Fore.RED + 'This is bold red text' + Style.RESET_ALL) """

# Question 2: How do you apply multiple styles (e.g., color and bold) to text using colorama?
# Answer: You can apply multiple styles by combining the style attributes (e.g., Style.BRIGHT + Fore.COLOR_NAME).

# Exercise 3: Print "This is red text" followed by "This is green text" on the next line.
# Guidelines:
# 1. Use \n to move to the next line.
""" print(Fore.RED + 'This is red text' + Style.RESET_ALL + '\n' + Fore.GREEN + 'This is green text' + Style.RESET_ALL) """

# Question 3: How do you reset the style after printing colored text?
# Answer: You reset the style by using Style.RESET_ALL after the colored text.

# Exercise 4: Write a function that takes a string and a color as arguments and prints the string in the specified color.
# Guidelines:
# 1. Define a function with parameters for the string and color.
""" def print_colored(text, color):
    print(color + text + Style.RESET_ALL)

print_colored('This is custom colored text', Fore.YELLOW) """

# Question 4: How do you pass arguments to a function in Python?
# Answer: You pass arguments to a function by specifying them in the parentheses when calling the function.

# Exercise 5: Modify the code to print "This is red text" in red and "This is normal text" in the default color on the same line.
# Guidelines:
# 1. Concatenate the strings with different styles.
""" print(Fore.RED + 'This is red text' + Style.RESET_ALL + ' This is normal text') """

# Question 5: How do you concatenate strings with different styles in Python?
# Answer: You concatenate strings with different styles by using the + operator to combine them.

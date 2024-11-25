# L1 = [1, 9, 1, 6, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 2]

# l = []
# for i in L1:
#     if i not in l : l.append(i)
# print(l)

# from functools import reduce

# ll = [1, 9, 1, 6, 3, 4]
# su = reduce(lambda x,y:x+y,ll)
# print(su)
# print(sum(ll))

# str= "amine"
# check = True
# for i in range(int(len(str) / 2)):
#     if str[i] != str[len(str) - i - 1]: check = False

# if check : print('Palindrome')
# else : print("Not Palindrome")

'''
Write a Python script that performs the following tasks:

Generate a random integer between -10,000 and 10,000.
Extract the last digit of the number, considering the sign of the number (i.e., if the number is negative, the last digit should also be negative).
Print a message in the following format:
"Last digit of <number> is <last_digit> and is":
If the last digit is greater than 5, append "greater than 5".
If the last digit is equal to 0, append "0".
If the last digit is less than 6 and not 0, append "less than 6 and not 0".

Example Output:
If the random number is -9234, the output would be:


Last digit of -9234 is -4 and is less than 6 and not 0
If the random number is 9837, the output would be:

Last digit of 9837 is 7 and is greater than 5
If the random number is 8400, the output would be:

Last digit of 8400 is 0 and is 0
This exercise practices:

Random number generation.
Extracting digits.
Conditional stateme
'''

import random
def get_last_digit():
    num = random.randint(-10000,10000)
    last_digit = abs(num) % 10

    if last_digit > 5 : check = " and is greater than 5"
    elif last_digit == 0 :check = " and is 0"
    elif last_digit < 6 : check = " and is less than 6 and not 0"
    res = f"Last digit of {num} is {last_digit}{check}"
    print(res)
# get_last_digit()


'''
Write a Python script that performs the following task:

Print the alphabet in lowercase, starting from a to z, without using any built-in alphabet constants.
Ensure that the output is not followed by a new line between characters (i.e., all letters should appear on the same line).
Requirements:
You must use the chr() function to convert ASCII values to their corresponding characters.
The output should not be followed by a new line or any extra spaces between the characters.
Example Output:
Copy code
abcdefghijklmnopqrstuvwxyz
This exercise practices:

Loops and ranges.
Using ASCII values.
Formatting print output to avoid newline characters
'''

def print_alpha():
    for i in range(97,123):
        print(chr(i),end="")
    print()
# print_alpha()


"""
Write a Python script that performs the following task:

Print the alphabet in lowercase, from a to z, excluding the letters q and e.
Ensure that the output is not followed by a new line between characters (i.e., all letters should appear on the same line).
Requirements:
Use a loop to iterate through the alphabet, and skip the letters q and e.
The output should not have any extra spaces or newlines between the printed characters.
Example Output:
Copy code
abcdfghijklmnoprstuvwxyz
This exercise practices:

Loops and ranges.
Conditional statements.
Skipping specific values within a range.
"""

def print_alpha_eq():
    for i in range(97,123):
        if chr(i) == "e" or chr(i) == "q":continue
        print(chr(i),end="")
    print()
# print_alpha_eq()


"""
Write a Python script that performs the following task:

Print the numbers from 0 to 98.
For each number, print both its decimal and hexadecimal representations in the following format:
<decimal> = <hexadecimal>.
Requirements:
Use a loop to iterate through the numbers.
Convert each number to its hexadecimal equivalent using the hex() function.
Ensure that both the decimal and hexadecimal representations appear on the same line.
Example Output:
python
Copy code
0 = 0x0
1 = 0x1
2 = 0x2
...
98 = 0x62
This exercise practices:

Looping over a range.
Using the hex() function to convert numbers to hexadecimal.
Formatting output in Python.
"""

def print_dec_hex():
    for i in range(0,99):
        print(f"{i} : {hex(i)}")
    print()
# print_dec_hex()


"""
Write a Python script that performs the following task:

Print the numbers from 0 to 99, ensuring that:
Each number is printed with at least two digits (e.g., 00, 01, ..., 09, 10, ..., 99).
Each number should be followed by a comma and a space, except for the last number (99), which should be printed on its own line without a trailing comma.
Requirements:
Use a loop to iterate through the numbers.
Use string formatting to ensure that each number is displayed with two digits.
Control the output format so that the last number is printed without a trailing comma.
Example Output:
Copy code
00, 01, 02, 03, 04, 05, 06, 07, 08, 09, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98
99
This exercise practices:

Looping over a range of numbers.
Formatting numbers with leading zeros.
Conditional statements to control output formatting
"""

def combo():
    for i in range(100):
        if i > 97 : print(f"{i:02}")
        else : print(f"{i:02}",end=", ")
# combo()


"""
Exercise:
Write a Python script that performs the following task:

Print all possible different combinations of two digits (from 0 to 9) in ascending order.
The two digits must be different (e.g., 01 and 10 are considered identical).
Ensure that the combinations are printed in the following format:
If the combination is not the last (i.e., 89), it should be followed by a comma and a space.
The combination 89 should be printed without a trailing comma.
Requirements:
Use nested loops to generate combinations of two digits.
Control the output format so that the last combination is printed correctly without a trailing comma.
Example Output:
Copy code
01, 02, 03, 04, 05, 06, 07, 08, 09, 12, 13, 14, 15, 16, 17, 18, 19, 23, 24, 25, 26, 27, 28, 29, 34, 35, 36, 37, 38, 39, 45, 46, 47, 48, 49, 56, 57, 58, 59, 67, 68, 69, 78, 79, 89
This exercise practices:

Nested loops to generate combinations.
String formatting for output.
Conditional statements to control formatting of the last item.
"""

def combo1():
    for i in range(9):
        k = i + 1
        for j in range(k,10):
            if i == 8 : print(f"{i}{j}")
            else : print(f"{i}{j}",end=", ")
# combo1()



"""
Here’s how you can frame the exercise whose answer would be the code you provided:

Exercise:
Write a Python function named islower that performs the following task:

Check if a given character is a lowercase letter.
The function should take a single character as an argument.
It should return True if the character is a lowercase letter (a to z), and False otherwise.
Requirements:
Use the ord() function to determine the ASCII value of the character.
The ASCII values for lowercase letters range from 97 ('a') to 122 ('z').
Example Usage:
python
Copy code
print(islower('a'))  # Output: True
print(islower('Z'))  # Output: False
print(islower('g'))  # Output: True
print(islower('1'))  # Output: False
This exercise practices:

Writing functions in Python.
Using conditional statements to evaluate conditions.
Understanding character encoding and the use of the ord() function.
"""
def is_lower(char):
    if ord(char) >= 97 and ord(char) <= 122 : return True
    return False
# print(is_lower("A"))


"""
Write a Python function named uppercase that performs the following task:

    Convert and print a string in uppercase:
        The function should take a single string as an argument.
        It should convert all lowercase letters in the string to uppercase (without using Python's built-in upper() function).
        After converting the string, print the result on a single line without changing any non-letter characters.

Requirements:

    Use the ord() function to determine the ASCII value of each character.
    Convert lowercase letters ('a' to 'z') to their uppercase equivalents by subtracting 32 from their ASCII values.
    Print the string without adding any newlines or spaces between characters, except for the final newline at the end.
"""

def to_upper(str):
    for i in str:
        if ord(i) >= 97 and ord(i) <= 127:
            up = ord(i) - 32
            print(chr(up),end="")
        else : print(i,end="")
# to_upper("aminE5")


"""
Write a Python function named print_last_digit that performs the following task:

    Print the last digit of a given integer:
        The function should take a single integer as an argument (which can be positive or negative).
        It should calculate the last digit of the number by taking the absolute value and using the modulus operator.
        Print the last digit without a newline after it.
    Return the last digit as an integer.

Requirements:

    Use the abs() function to ensure the last digit is positive, regardless of whether the input number is positive or negative.
    Use the modulus operator (%) to extract the last digit.

Example Usage:

python

last_digit = print_last_digit(123)    # Output: 3
print(last_digit)                      # Output: 3
last_digit = print_last_digit(-456)   # Output: 6
print(last_digit)                      # Output: 6

Explanation:

    The function calculates the last digit of the provided number, prints it immediately, and then returns the digit for potential further use.

This exercise practices:

    Function definition and return values.
    Using mathematical operations to manipulate numbers.
    Printing output without automatically adding a newline.
"""


def print_last_digit1(num):
    ls = abs(num)%10
    print(ls)
    return ls
# print(print_last_digit1(4545))

"""
Write a Python script that performs the following task:

Print the alphabet in reverse order, starting from z to a, alternating between uppercase and lowercase letters.
The first letter printed should be z (lowercase), the second should be Y (uppercase), then x (lowercase), and so on.
Requirements:
Use a loop to iterate through the ASCII values of the letters from z to a.
Alternate the case of each letter by adjusting the ASCII value based on a flag or condition.
Example Output:
Copy code
zYxWvUtSrQpOnMlKjIhGfEdCbA
Explanation:
The script uses the ord() function to get the ASCII values for z and a and iterates in reverse order.
It uses the chr() function to convert the ASCII values back to characters.
The variable i is used to toggle between uppercase and lowercase by adjusting the ASCII value by 32 when needed.
This exercise practices:

"""


def print_z_to_a():
    for i in range(122,96,-1):
        if i % 2 : print(chr(i - 32),end="")
        else : print(chr(i),end="")
# print_z_to_a()



"""
Write a Python function named remove_char_at that performs the following task:

Create a copy of a string without the character at a specified position:
The function should take two arguments:
str: the original string.
n: the index of the character to be removed.
If n is a negative index, return the original string unchanged.
If n is a valid index, return a new string that excludes the character at that index.
Requirements:
Use string slicing to construct the new string without the specified character.
Ensure that the function handles negative indices appropriately by returning the original string.
Example Usage:
python
Copy code
print(remove_char_at("Hello", 1))  # Output: "Hllo"
print(remove_char_at("World", 4))  # Output: "Worl"
print(remove_char_at("Python", -1)) # Output: "Python"
"""

def remove_char_at(str,index):
    newstr = ""
    for i in range(len(str)):
        if i is not index : newstr = newstr + str[i]
    return newstr
# print(remove_char_at("amine",0))

def fizz_buss():
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0 : print("fizzbuzz")
        elif i % 3 == 0 : print("fizz")
        elif i % 5 == 0 : print("buzz")
        else : print(i)

# fizz_buss()

"""
Write a Python script that imports functions from a module named calculator_1. The script should:

    Define two variables, a and b, with values 10 and 5, respectively.
    Print the sum, difference, product, and quotient of a and b using the imported functions:
        add(a, b)
        sub(a, b)
        mul(a, b)
        div(a, b)

Make sure to format the output to clearly show the operation being performed, for example, "10 + 5 = 15".

Additionally, ensure you include the calculator_1 module, which should contain the definitions for the add, sub, mul, and div functions.
"""
# from calc import *
# a = 5
# b = 0

# add(a,b)
# sub(a,b)
# mul(a,b)
# div(a,b)



"""
Here’s the corresponding exercise based on your answer:

### Exercise:
Write a Python script that imports a module named `hidden_4` and prints all names defined in that module, excluding any names that start with double underscores (`__`). The script should:

1. Import the `hidden_4` module.
2. Use the `dir()` function to retrieve a list of all names defined in the module.
3. Loop through the list of names, and for each name:
   - Check if it does not start with `__`.
   - If it meets the condition, print the name.

Ensure that the `hidden_4` module is available and contains several defined names to demonstrate the functionality of your script.
"""

import hidden

all = dir(hidden)
for i in all :
    if not i.startswith("__"):
        print(i)
print(hidden.a)


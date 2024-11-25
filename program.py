#!/usr/bin/python3

"""
Write a Python script that counts and displays the number of command-line arguments provided to it. The script should:

    Import the sys module.
    Count the number of command-line arguments (excluding the script name) and store this count in a variable.
    Print a message based on the count of arguments:
        If there are no arguments, print:

0 arguments.

If there is one argument, print:

1 argument:

If there are multiple arguments, print:

    <count> arguments:

Loop through the arguments and print each one in the format:

    <index>: <argument>

    where <index> is the position of the argument (starting from 1).

Make sure to test the script with different numbers of command-line arguments to verify its functionality.
You said:

"""

import sys

if __name__ == "__main__":
    # print(sys.argv)
    count = len(sys.argv)
    if count == 1: print("0 arguments.")
    elif count == 2 : print("1 argument")
    else :
        print(f"{count-1} arguments:")
        for i in range(1,count):
            print(f"{i} :  {sys.argv[i]}")
    
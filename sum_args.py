#!/usr/bin/python3
import sys
"""
Create a Python script that calculates and prints the sum of all command-line arguments passed to it. The script should:

    Import the sys module.
    Initialize a variable total to zero.
    Loop through the command-line arguments (excluding the script name) and convert each argument to an integer, adding it to the total.
    Print the total sum of the arguments.

Make sure to test the script with various sets of numerical command-line arguments to confirm its correctness.
"""

if __name__ == "__main__":
    if len(sys.argv) == 1: print("Please provide some numbers :)");sys.exit(1)
    try:
        total = 0
        for i in range(1,len(sys.argv)):
            total += float(sys.argv[i])
        print("Total is : {}".format(total))
    except ValueError :
        print("Please enter just numbers :)")
    finally :
        sys.exit(0)
        
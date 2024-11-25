#!/usr/bin/python3

"""
Here's the corresponding exercise based on your answer:

### Exercise:
Create a Python script that performs basic arithmetic operations based on user input. The script should:

1. Import the functions `add`, `sub`, `mul`, and `div` from a module named `calculator_1`.
2. Check if the correct number of command-line arguments (three) is provided. If not, print the usage message: 
   ```
   Usage: ./100-my_calculator.py <a> <operator> <b>
   ```
   and exit the program.
3. Define a dictionary `ops` that maps operators (`+`, `-`, `*`, `/`) to their corresponding functions from the `calculator_1` module.
4. Check if the operator provided is valid (i.e., one of the keys in `ops`). If not, print an error message:
   ```
   Unknown operator. Available operators: +, -, * and /
   ```
   and exit the program.
5. Convert the first and third command-line arguments to integers and store them in variables `a` and `b`.
6. Print the result of the arithmetic operation in the format:
   ```
   <a> <operator> <b> = <result>
   ```

Make sure to implement the `calculator_1` module that contains the definitions for the `add`, `sub`, `mul`, and `div` functions.
"""
import sys
from calc1 import *
if __name__ == "__main__":
    if len(sys.argv) != 4 :
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    opers = {"/":div,"+":add,"-":sub,"*":mul,"x":mul}
    if sys.argv[2] not in opers:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    try : 
        a = float(sys.argv[1])
        b = float(sys.argv[3])
        opers[sys.argv[2]](a,b)
    except :
        print("Enter valid numbers")
        sys.exit(1)
    sys.exit(0)
    # match sys.argv[2]:
    #     case "+" : add(a,b)
    #     case "-" : sub(a,b)
    #     case "/" : div(a,b)
    #     case "*": mul(a,b)
    #     case "x": mul(a,b)


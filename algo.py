"""
Exercise: Element Retrieval from a List

Write a Python function called element_at that retrieves an element from a list based on the provided index.

Requirements:

    The function should take two parameters:
        my_list: A list from which to retrieve the element.
        idx: An integer index indicating the position of the element to retrieve.
    If the index is negative or greater than the last index of the list, the function should return None.
    Otherwise, return the element at the specified index in the list.

Example Usage:

python

my_list = [10, 20, 30, 40, 50]
print(element_at(my_list, 2))  # Output: 30
print(element_at(my_list, 5))  # Output: None
print(element_at(my_list, -1))  # Output: None
"""

def element_at(my_list, idx):
    if idx > (len(my_list)-1) : return None
    if idx < 0 : return None
    return my_list[idx]

# l = ["amine","ben","omar"]
# print(element_at(l,0))

"""
Write a Python function called replace_in_list that replaces an element in a list at a specified index.

Requirements:

    The function should take three parameters:
        my_list: A list in which you want to replace an element.
        idx: An integer index indicating the position of the element to replace.
        element: The new element that will replace the old element at the specified index.
    If the index is valid (i.e., it is greater than or equal to 0 and less than the length of the list), replace the element at that index with the new element.
    If the index is invalid, leave the list unchanged.
    Return the modified list.

Example Usage:

python

my_list = [10, 20, 30, 40, 50]
print(replace_in_list(my_list, 2, 99))  # Output: [10, 20, 99, 40, 50]
print(replace_in_list(my_list, 5, 99))  # Output: [10, 20, 99, 40, 50] (no change)

"""

def replace_in_list(l,i,e):
    if i >= 0 and not(i > len(l)-1):
        l[i] = e
    return l

# my_list = [10, 20, 30, 40, 50]
# print(replace_in_list(my_list, 2, 99))  # Output: [10, 20, 99, 40, 50]
# print(replace_in_list(my_list, 5, 99))  # Output: [10, 20, 99, 40, 50] (no change)


"""
Write a Python function called print_reversed_list_integer that prints all integers from a list in reverse order.

Requirements:

    The function should take one parameter:
        my_list: A list of integers (default is an empty list).
    Check if the parameter is indeed a list. If it is, reverse the list and print each integer in the reversed list.
    Each integer should be printed on a new line, formatted as an integer (without any additional formatting).

Example Usage:

python

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)
# Output:
# 5
# 4
# 3
# 2
# 1

print_reversed_list_integer()  # No output (empty list)
"""

def print_reversed_list_integer(l):
    if isinstance(l,list):
        ll = len(l) - 1
        while ll >= 0:
            print(l[ll])    
            ll-=1
    else : print("Please provide a list")

# print_reversed_list_integer([1, 2, 3, 4, 5])


"""
Write a Python function called new_in_list that creates a copy of a list and replaces an element at a specified index in the copied list.

Requirements:

    The function should take three parameters:
        my_list: The original list from which to create a copy.
        idx: An integer index indicating the position of the element to replace in the copied list.
        element: The new element that will replace the old element at the specified index in the copied list.

    If the index is negative or greater than the last index of the list, return the original list unchanged.

    Otherwise, create a copy of the original list, replace the element at the specified index with the new element, and return the modified copy.

Example Usage:

python

my_list = [10, 20, 30, 40, 50]
new_list = new_in_list(my_list, 2, 99)
print(new_list)  # Output: [10, 20, 99, 40, 50]
print(my_list)   # Output: [10, 20, 30, 40, 50] (original list unchanged)

print(new_in_list(my_list, 5, 99))  # Output: [10, 20, 30, 40, 50] (no change)
print(new_in_list(my_list, -1, 99))  # Output: [10, 20, 30, 40, 50] (no change)
"""

def new_in_list(l,i,e):
    if i < 0 or i >= len(l):
        return l
    else :
        new_list = l[:]
        new_list[i] = e
        return new_list

# my_list = [10, 20, 30, 40, 50]
# new_list = new_in_list(my_list, 2, 99)
# print(new_list)  # Output: [10, 20, 99, 40, 50]
# print(my_list)   # Output: [10, 20, 30, 40, 50] (original list unchanged)

# print(new_in_list(my_list, 5, 99))  # Output: [10, 20, 30, 40, 50] (no change)
# print(new_in_list(my_list, -1, 99))  # Output: [10, 20, 30, 40, 50] (no change)


"""
Write a Python function called no_c that removes all occurrences of the characters 'c' and 'C' from a given string.

Requirements:

    The function should take one parameter:
        my_string: A string from which to remove the specified characters.
    Create a new string that contains all characters from the original string, except for 'c' and 'C'.
    Return the modified string.

Example Usage:

python

print(no_c("Chocolate is cool."))  # Output: "hoolate is ool."
print(no_c("Caterpillar"))          # Output: "aterpillar"
print(no_c("No characters here!"))  # Output: "No haraters here!"
"""
def no_c(str):
    new =""
    for i in range(len(str)):
        if str[i] == "c" or str[i] == "C":
            continue
        new = new + str[i]
    return new

# print(no_c("Chocolate is cool."))  # Output: "hoolate is ool."
# print(no_c("Caterpillar"))          # Output: "aterpillar"
# print(no_c("No characters here!"))  # Output: "No haraters here!"


"""
Write a Python function called print_matrix_integer that prints a matrix (a list of lists) of integers.

Requirements:

    The function should take one parameter:
        matrix: A list of lists containing integers (default is a matrix with an empty list).
    Each integer in the matrix should be printed, and each row should be printed on a new line.
    The integers in each row should be separated by a space, but there should be no trailing space after the last integer of each row.

Example Usage:

python

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print_matrix_integer(matrix)
# Output:
# 1 2 3
# 4 5 6
# 7 8 9

print_matrix_integer([[]])  # Output: (prints an empty line)
"""

def print_matrix_integer(matrix):
    for i in matrix:
        for j in i:
            print(j,end=" ")
        print()

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print_matrix_integer(matrix)
# print_matrix_integer([[]])


"""
Write a Python function called add_tuple that adds two tuples element-wise.

Requirements:

    The function should take two parameters:
        tuple_a: The first tuple (default is an empty tuple).
        tuple_b: The second tuple (default is an empty tuple).
    Each tuple can contain up to two elements. If a tuple has fewer than two elements, assume the missing values are 0.
    If a tuple is empty, treat it as (0, 0).
    The function should return a new tuple that contains the sum of the first elements of both tuples and the sum of the second elements of both tuples.

Example Usage:

print(add_tuple((1, 2), (3, 4)))    # Output: (4, 6)
print(add_tuple((1,), (2, 3)))       # Output: (3, 3)
print(add_tuple((), (1,)))            # Output: (1, 0)
print(add_tuple((5, 6), ()))          # Output: (5, 6)
print(add_tuple())                    # Output: (0, 0)
"""

def check(t,i):
    try:
        return t[i]
    except Exception as e:
        return 0
    
def add_tuple(t1 = (),t2 = ()):
    return tuple([check(t1,0)+check(t2,0),
                  check(t1,1)+check(t2,1)])

# print(add_tuple((1, 2), (3, 4)))    # Output: (4, 6)
# print(add_tuple((1,), (2, 3)))       # Output: (3, 3)
# print(add_tuple((), (1,)))            # Output: (1, 0)
# print(add_tuple((5, 6), ()))          # Output: (5, 6)
# print(add_tuple())                    # Output: (0, 0)


"""
Write a Python function called multiple_returns that returns the length of a string and its first character.

Requirements:

    The function should take one parameter:
        sentence: A string for which you want to obtain the length and the first character.
    If the string is empty, the function should return a tuple containing 0 and None.
    Otherwise, return a tuple containing the length of the string and its first character.

Example Usage:

python

print(multiple_returns("Hello"))       # Output: (5, 'H')
print(multiple_returns("Python"))      # Output: (6, 'P')
print(multiple_returns(""))             # Output: (0, None)
print(multiple_returns("A"))            # Output: (1, 'A')
"""

def multiple_returns(strr=""):
    if isinstance(strr,str) and len(strr) > 0:
        return len(strr), strr[0]
    else :
        return 0,None
# print(multiple_returns("Hello"))       # Output: (5, 'H')
# print(multiple_returns("Python"))      # Output: (6, 'P')
# print(multiple_returns(""))             # Output: (0, None)
# print(multiple_returns("A"))            # Output: (1, 'A')


"""
Write a Python function called max_integer that finds the largest integer in a given list.

Requirements:

    The function should take one parameter:
        my_list: A list of integers (default is an empty list).
    If the list is empty, return None.
    Otherwise, iterate through the list and find the largest integer, returning it.

Example Usage:

python

print(max_integer([1, 2, 3, 4, 5]))  # Output: 5
print(max_integer([-10, -20, -3]))    # Output: -3
print(max_integer([7, 7, 7]))          # Output: 7
print(max_integer([]))                  # Output: None
"""

def max_integer(arr = []):
    if isinstance(arr,list) and len(arr) > 0:
        return max(arr)
    else :
        return None
def max_integer1(arr = []):
    if isinstance(arr,list) and len(arr) > 0:
        s = sorted(arr)
        return s[-1]
    else :
        return None 

# print(max_integer([1, 2, 3, 4, 5]))  # Output: 5
# print(max_integer([-10, -20, -3]))    # Output: -3
# print(max_integer([7, 7, 7]))          # Output: 7
# print(max_integer([]))                  # Output: None


# print(max_integer1([1, 2, 3, 4, 5]))  # Output: 5
# print(max_integer1([-10, -20, -3]))    # Output: -3
# print(max_integer1([7, 7, 7]))          # Output: 7
# print(max_integer1([]))                  # Output: None


"""
Write a Python function called divisible_by_2 that checks which integers in a list are divisible by 2.

Requirements:

    The function should take one parameter:
        my_list: A list of integers (default is an empty list).
    Create a new list that contains True for each integer in my_list that is divisible by 2 and False for those that are not.
    Return the new list.

Example Usage:

python

print(divisible_by_2([1, 2, 3, 4, 5]))  # Output: [False, True, False, True, False]
print(divisible_by_2([10, 21, 32, 43]))  # Output: [True, False, True, False]
print(divisible_by_2([]))                 # Output: []
"""

def divisible_by_2(l=[]):
    return [True if i % 2 == 0 else False for i in l]

# print(divisible_by_2([1, 2, 3, 4, 5]))  # Output: [False, True, False, True, False]
# print(divisible_by_2([10, 21, 32, 43]))  # Output: [True, False, True, False]
# print(divisible_by_2([]))                 # Output: []


"""
Write a Python function called delete_at that deletes an item at a specified index from a list.

Requirements:

    The function should take two parameters:
        my_list: A list from which you want to delete an item (default is an empty list).
        idx: An integer index indicating the position of the item to delete (default is 0).
    If the index is valid (i.e., it is greater than or equal to 0 and less than the length of the list), delete the item at that index.
    If the index is invalid, leave the list unchanged.
    Return the modified list.

Example Usage:

python

my_list = [10, 20, 30, 40, 50]
print(delete_at(my_list, 2))  # Output: [10, 20, 40, 50]
print(delete_at(my_list, 5))   # Output: [10, 20, 40, 50] (no change)
print(delete_at(my_list, -1))  # Output: [10, 20, 40, 50] (no change)
"""

def delete_at(l,i):
    if i >= 0 and i < len(l):
        del l[i]
    return l
# my_list = [10, 20, 30, 40, 50]
# print(delete_at(my_list, 2))  # Output: [10, 20, 40, 50]
# print(delete_at(my_list, 5))   # Output: [10, 20, 40, 50] (no change)
# print(delete_at(my_list, -1))  # Output: [10, 20, 40, 50] (no change)


"""
Write a Python function named square_matrix_simple that takes a matrix (a list of lists) as an argument and returns a new matrix where each element of the original matrix is squared. The function should not modify the original matrix.

Requirements:

    The input matrix will be a list of lists containing integers or floats.
    The function should return a new matrix with the same dimensions, with each element squared.

Example:

python

matrix = [[1, 2, 3], [4, 5, 6]]
print(square_matrix_simple(matrix))
# Output: [[1, 4, 9], [16, 25, 36]]

Make sure to handle edge cases, such as an empty matrix.
"""

def square_matrix_simple(mat = []):
    new_mat = []
    for i in mat:
        l = []
        for j in i:
            l.append(j**2)
        new_mat.append(l)
    return new_mat

# matrix = [[1, 2, 3], [4, 5, 6]]
# print(square_matrix_simple(matrix))
# print(square_matrix_simple([]))
# Output: [[1, 4, 9], [16, 25, 36]]


"""
Write a Python function named search_replace that takes three arguments: a list my_list, a value search, and a value replace. The function should return a new list where all occurrences of search in my_list are replaced with replace.

Requirements:

    The input list can contain any data type.
    The function should not modify the original list.

Example:

python

my_list = [1, 2, 3, 2, 4]
print(search_replace(my_list, 2, 99))
# Output: [1, 99, 3, 99, 4]

Make sure to handle cases where search is not found in the list (the original list should remain unchanged
"""
def search_replace(l,v,r):
    if isinstance(l,list) and isinstance(v,int) and isinstance(r,int):
        new = l[:]
        for i in range(len(new)):
            if new[i] == v : new[i] = r
        return new
    else : print("Invalid inputs");return l

# my_list = [1, 2, 3, 2, 4]
# print(search_replace(my_list, 2, 99))
# print(my_list)
# Output: [1, 99, 3, 99, 4]



"""
Function Name: to_subtract

Description: Write a Python function named to_subtract that takes a list of numbers as input and calculates the maximum value in the list. It should then subtract the sum of all other numbers from this maximum value and return the result.

Requirements:

    The function should return 0 if the input list is empty.
    The function should handle both positive and negative numbers.

Example:

python

list_num = [1, 2, 3, 4]
print(to_subtract(list_num))
# Output: 4 - (1 + 2 + 3) = -2
"""
def to_subtract(l=[]):
    if len(l) == 0 or not(isinstance(l,list)) : return 0
    max_value = l[0]
    for i in l:
        if i > max_value : max_value = i
    
    total = 0
    st=""
    c = 0
    for i in l:
        if i != max_value : 
            if c < len(l) - 2 : 
                st = st + str(i) + " + "
            else : 
                st = st + str(i)
            total = total + i
            c+=1

    print(f"{max_value} - ({st}) = {max_value - total}")

# list_num = [1, 2, 3, 4]
# print(to_subtract(list_num))
# Output: 4 - (1 + 2 + 3) = -2

"""
Description: Write a Python function named uniq_add that takes a list of numbers as input and returns the sum of all unique numbers in the list.

Requirements:

    The function should handle any type of numbers (integers or floats).
    If the input list is empty, the function should return 0.
    The function should not modify the original list.

Example:

python

my_list = [1, 2, 3, 2, 4]
print(uniq_add(my_list))
# Output: 10 (1 + 2 + 3 + 4 = 10)

Make sure to clarify how duplicates in the input list should be handled!
"""

def uniq_add(l=[]):
    if isinstance(l,list):
        ll = []
        for i in l :
            if i not in ll : ll.append(i)
        return sum(ll)
    else :
        print("provide list");return None

# my_list = [1, 2, 3, 2, 4]
# print(uniq_add(my_list))
# Output: 10 (1 + 2 + 3 + 4 = 10)

"""
Function Name: common_elements

Description: Write a Python function named common_elements that takes two sets as arguments and returns a set containing the elements that are common to both sets.

Requirements:

    The function should return an empty set if there are no common elements.
    The function should handle sets with different data types.



Feel free to adjust the details as needed!
"""

def common_elements(s1=set(),s2=set()):
    return s2 & s1

# set_1 = {1, 2, 3, 4}
# set_2 = {3, 4, 5, 6}
# print(common_elements(set_1, set_2))
# # Output: {3, 4}

# set_a = {'a', 'b', 'c'}
# set_b = {'d', 'e', 'f'}
# print(common_elements(set_a, set_b))
# print(common_elements())
# # Output: set()


"""
Function Name: only_diff_elements

Description: Write a Python function named only_diff_elements that takes two sets as arguments and returns a set containing the elements that are present in either of the sets but not in both.

Requirements:

    The function should return a new set with the unique elements from both sets.
    If there are no unique elements, the function should return an empty set.

Example:

python

set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
print(only_diff_elements(set_1, set_2))
# Output: {1, 2, 5, 6}

set_a = {'a', 'b', 'c'}
set_b = {'b', 'c', 'd'}
print(only_diff_elements(set_a, set_b))
# Output: {'a', 'd'}

"""

def only_diff_elements(s1=set(),s2=set()):
    return s1 ^ s2


"""
Function Name: number_keys

Description: Write a Python function named number_keys that takes a dictionary as an argument and returns the number of keys in that dictionary.

Requirements:

    The function should return 0 if the dictionary is empty.
    The function should handle dictionaries with any data types for keys and values.

Example:

python

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(number_keys(my_dict))
# Output: 3

empty_dict = {}
print(number_keys(empty_dict))
# Output: 0

Feel free to adjust the details as needed!
"""
def number_keys(d):
    return len(d)


"""
Function Name: number_keys

Description: Write a Python function named number_keys that takes a dictionary as an argument and returns the number of keys in that dictionary.

Requirements:

    The function should return 0 if the dictionary is empty.
    The function should work with dictionaries containing any data types for keys and values.

Example:

python

my_dict = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
print(number_keys(my_dict))
# Output: 3

empty_dict = {}
print(number_keys(empty_dict))
# Output: 0

Feel free to modify any part of the exercise as needed!
"""

def number_keys(d):
    return len(d)

"""
Function Name: update_dictionary

Description: Write a Python function named update_dictionary that takes a dictionary, a key, and a value as arguments. The function should update the dictionary by replacing the value of the specified key if it exists, or adding the key/value pair if the key does not exist. The function should return the updated dictionary.

Requirements:

    If the key already exists in the dictionary, its value should be replaced with the new value.
    If the key does not exist, it should be added to the dictionary.

my_dict = {'name': 'Alice', 'age': 30}
print(update_dictionary(my_dict, 'age', 31))
# Output: {'name': 'Alice', 'age': 31}

print(update_dictionary(my_dict, 'city', 'Wonderland'))
# Output: {'name': 'Alice', 'age': 31, 'city': 'Wonderland'}

"""

def update_dictionary(d,k,v):
    d.update({k:v})
    return d

"""

Description: Write a Python function named simple_delete that takes a dictionary and a key as arguments. The function should remove the specified key from the dictionary if it exists and return the updated dictionary. If the key does not exist, the dictionary should remain unchanged.

Requirements:

    If the key is present in the dictionary, it should be deleted.
    If the key is not present, the function should not modify the dictionary.
    The function should return the updated dictionary.

Example:

python

my_dict = {'name': 'Alice', 'age': 30, 'city': 'Wonderland'}
print(simple_delete(my_dict, 'age'))
# Output: {'name': 'Alice', 'city': 'Wonderland'}

print(simple_delete(my_dict, 'country'))
# Output: {'name': 'Alice', 'age': 30, 'city': 'Wonderland'} (no change)
"""
def simple_delete(d,k):
    if k in d :
        del d[k]
    return d


"""
Function Name: multiply_by_2

Description: Write a Python function named multiply_by_2 that takes a dictionary as an argument and returns a new dictionary where all the values are multiplied by 2. The original dictionary should remain unchanged.

Requirements:

    The function should create and return a new dictionary.
    It should handle dictionaries with integer or float values.

Example:

python

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(multiply_by_2(my_dict))
# Output: {'a': 2, 'b': 4, 'c': 6}

print(my_dict)
# Output: {'a': 1, 'b': 2, 'c': 3} (original dictionary remains unchanged)

"""

def multiply_by_2(d = {}):
    new = d.copy()
    for key,value in new.items():
        new[key] = value*2
    return new


"""
Function Name: multiply_list_map

Description: Write a Python function named multiply_list_map that takes a list and a number as arguments and returns a new list with each element of the original list multiplied by the given number.

Requirements:

    The function should return a new list, leaving the original list unchanged.
    It should handle both integers and floats in the list.

Example:

python

my_list = [1, 2, 3, 4]
number = 3
print(multiply_list_map(my_list, number))
# Output: [3, 6, 9, 12]

my_list = [1.5, 2.5, 3.5]
number = 2
print(multiply_list_map(my_list, number))
# Output: [3.0, 5.0, 7.0]
"""
def multiply_list_map(l=[],n=1):
    return list(map(lambda x: x*n,l))


"""
Function Name: weight_average

Description: Write a Python function named weight_average that takes a list of tuples as an argument. Each tuple contains two values: a number and its corresponding weight. The function should return the weighted average of the numbers. If the list is empty, the function should return 0.

Requirements:

    Each tuple in the list should have the form (number, weight).
    The function should calculate the weighted average by dividing the total weighted sum of the numbers by the total weight.
    The function should handle cases where the total weight is zero.

Example:

python

my_list = [(10, 2), (20, 3), (30, 5)]
print(weight_average(my_list))
# Output: 22.5 (calculated as (10*2 + 20*3 + 30*5) / (2 + 3 + 5))

empty_list = []
print(weight_average(empty_list))
# Output: 0

"""

def weight_average(l=[]):
    if len(l) == 0 : return 0
    total_weight = 0
    avg = 0
    for i in l :
        total_weight =  total_weight + i[1]
        avg = avg + (i[0] * i[1])
    return avg / total_weight

# my_list = [(10, 2), (20, 3), (30, 5)]
# print(weight_average(my_list))
 # Output: 22.5 (calculated as (10*2 + 20*3 + 30*5) / (2 + 3 + 5))

# empty_list = []
# print(weight_average(empty_list))
# Output: 0


"""
Function Name: square_matrix_map

Description: Write a Python function named square_matrix_map that takes a matrix (a list of lists) as an argument and returns a new matrix where each element of the original matrix is squared. The function should not modify the original matrix.

Requirements:

    The input matrix will be a list of lists containing integers or floats.
    The function should return a new matrix with the same dimensions, with each element squared.

Example:

python

matrix = [[1, 2, 3], [4, 5, 6]]
print(square_matrix_map(matrix))
# Output: [[1, 4, 9], [16, 25, 36]]

matrix_empty = []
print(square_matrix_map(matrix_empty))
# Output: [] (empty matrix)
"""
def square_matrix_map(mat = []):
    new = []
    for i in mat :
        l = []
        for j in i :
            l.append(j**2)
        new.append(l)
    return new


"""
Function Name: complex_delete

Description: Write a Python function named complex_delete that takes a dictionary and a value as arguments. The function should delete all keys in the dictionary that have the specified value and return the updated dictionary.

Requirements:

    The function should modify the original dictionary.
    If the specified value is not found in the dictionary, it should remain unchanged.

Example:

python

my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3}
print(complex_delete(my_dict, 1))
# Output: {'b': 2, 'd': 3}

print(complex_delete(my_dict, 5))
# Output: {'b': 2, 'd': 3} (no change)
"""

def complex_delete(d,v):
    keys = []
    for i in d:
        if d[i] == v:
            keys.append(i)
    for key in keys:
        del d[key]
    return d


"""
Function Name: roman_to_int

Description: Write a Python function named roman_to_int that converts a Roman numeral string into an integer. The function should handle valid Roman numeral strings and return 0 for invalid input or an empty string.

Requirements:

    The function should only accept strings as valid input. If the input is not a string or if it is empty, it should return 0.
    The Roman numerals must be valid, and the function should correctly account for subtractive combinations (e.g., IV for 4, IX for 9).

Example:

python

roman_string = "MCMXCIV"
print(roman_to_int(roman_string))
# Output: 1994
"""
def roman_to_int(roman =""):
    if not roman or isinstance(roman,str) or roman.islower() or not roman.isalpha: return 0
    
    
#!/usr/bin/python3

class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

    def __str__(self) -> str:
        return f"{self.data}"
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = node
    
    def pop(self):
        if not self.head :
            print("Array is empty")
            return

        if not self.head.next:
            self.head = None
            return

        last = self.head
        while last.next.next:
            last = last.next
        last.next = None
    
    def print_list(self):
        if self.head == None:
            print("List is empty")
            return
    
        curr = self.head
        while curr:
            print(curr.data,end=" -> ")
            curr = curr.next
        print("None")
    

def reverse_linked_list(head):
    prev = None
    current = head
    while current :
            tmp = current.next
            current.next = prev
            prev = current
            current = tmp 
    return prev

def check_if_cycle(l):
    if not l.head or not l.head.next:
        return False
    
    fast = l.head
    slow = l.head
    while fast:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

# l = LinkedList()
# l.append(4)
# l.append(5)
# l.append(6)

# l.head.next.next.next = l.head.next

# print(check_if_cycle(l)) 

def linked_lem(l):
    cout = 0
    curr = l.head
    while curr:
        curr = curr.next
        cout += 1
    return cout

# print(linked_lem(l))


def find_middle_element(l):
    if not l.head :
        print("List is empty !")
        return

    fast = l.head
    slow = l.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow


# print(find_middle_element(l))

def find_start_of_cycle(l):
    check = False
    fast = l.head
    slow = l.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast :
            check =  True
            break

    if not check : return

    fast = l.head 
    while slow != fast:
        slow = slow.next    
        fast = fast.next
    return slow



class Stack():
    def __init__(self):
        self.head = None
    
    def push(self,value):
        node = Node(value)
        if not self.head :
            self.head = node
        else :
            curr = self.head
            while curr.next :
                curr = curr.next
            curr.next = node
    
    def pop(self):
        if not self.head:
            return
        if not self.head.next:
            tmp = self.head
            self.head = None
            return tmp
        
        curr = self.head
        while curr.next :
            if not curr.next.next:
                tmp = curr.next
                curr.next = None
                return tmp 
            curr = curr.next

        
    def peek(self):
        if not self.head:
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr


class Queue(LinkedList):
    def __init__(self):
        self.head = None

    def enqueue(self,value):
        node = Node(value)
        if not self.head : self.head= node;return
        tmp = self.head
        self.head = node
        self.head.next = tmp

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            return node.data
        current  = self.head
        while current.next:
            current = current.next
        current.next = node
        return node.data

    def dequeue(self):
        if not self.head :
            return None
        head = self.head 
        self.head = self.head.next
        return head



def is_balanced(s):
    stack = []
    for i in s:
        if i in "({[":
            stack.append(i)
        elif i in ")}]":
            if not stack or (i == ")" and "(" != stack[-1]) or (i == "}" and "{" != stack[-1]) or (i == "]" and "[" != stack[-1]) :
                return False
            else :
                stack.pop()
    return not stack


def have_common_elements(arr1,arr2):
    return len(set(arr1 +  arr2)) != len(arr1) + len(arr2)

def first_non_repeating_char(s):
    for i in s:
        if s.count(i) == 1:
            return i
        

# s = "swiss"
# result = first_non_repeating_char(s)  # Should return 'w'
# print(result)  # Output: w

# s = "aabbcc"
# result = first_non_repeating_char(s)  # Should return None
# print(result)  # Output: None

def is_unique(s):
    d = {}
    for i in s :
        if i not in d : d[i] = 1
        else : d[i] = d[i] + 1
    for j in d :
        if d[j] > 1:
            return False
    return True

# s = "abcdef"
# result = is_unique(s)  # Should return True
# print(result)  # Output: True

# s = "hello"
# result = is_unique(s)  # Should return False
# print(result)  # Output: False



def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) //2
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else :
            left = mid + 1
    return -1

# arr = [1, 3, 5, 7, 9, 11]
# target = 7
# index = binary_search(arr, target)
# print(index)  # Output: 3

# target = 4
# index = binary_search(arr, target)
# print(index)  # Output: -1

def smallest_missing_positive(l):
    new = l[:]
    for i in range(len(new)):
        if new[i] <= 0:
            del l[i]
    i = 1 
    while i <= max(l) + 1:
        if i not in l :
            return i
        i += 1
        

def gcd(a, b) :
    if a == 0 :
        return b
    if b == 0 :
        return a
    m = min(abs(a),abs(b))
    while m >= 1:
        if not a%m and not b%m:
            return m
        m -= 1


def factorial(n):
    if n == 0 or n == 1:
        return 1
    f = 1
    while n >= 2:
        f *= n
        n -= 1
    return f

def fac(n):
    if n == 1 or n == 0:
        return 1
    return n * fac(n - 1)


def is_prime(n):
    if n == 1 or n == 0 or n < 0:
        return False

    i = 2
    while i < n:
        if not n % i:
            return False
        i += 1
    return True

# Example test code
# n = 5
# Output: 0, 1, 1, 2, 3

def f(n):
    if n == 0 :
        return 0
    if n == 1:
        return 1
    return f(n - 1) + f(n- 2)

def fibonacci(n):
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    return (fibonacci(n - 1) + fibonacci(n - 2))

def function_li3ad3ta9ni(n):
    if n < 0:
        return
    if n==0:
        print("0", end="")
        return
    
    function_li3ad3ta9ni(n-1)

    if n > 0:
        print(", " , end="")
    
    print(f"{fibonacci(n)}", end="")

def fibonacci_sequence(n):
    function_li3ad3ta9ni(n-1)

    
# fibonacci_sequence(12)


def amine(n):
    i = 0
    while i < n:
        if i != 0:
            print(", ",end="")
        print(fibonacci(i),end="")
        i += 1
# amine(5)

def sum_of_digits(n):
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)

# n = 12345
# result = sum_of_digits(n)  
# print(result)  # Output: 15

def reverse_string(s):
    new = ""
    for i in reversed(range(len(s))):
        new += s[i]
    print(new)

def rev(s):
    l = 0
    for _ in s:
        l += 1
    new = ""
    while l >= 0:
        new += s[l]
        l -= 1
    print(new)
# reverse_string("amine")

def count_vowels_consonants(s):
    d = {"vow":0,"con":0}
    for i in s:
        if i.isalpha():
            if i in "aeuioy":d["vow"] += 1
            else : d["con"] +=1
    return d
# print(count_vowels_consonants("amine"))


def find_longest_word(s):
    words = {}
    i = 0
    m = ""
    while i < len(s):
        while  i < len(s) and  s[i] == " ":
            i += 1
        word = ""
        le = 0
        while  i < len(s) and s[i] != " ":
            word += s[i]
            le += 1
            i += 1
        words[word] = le
        m = word

    for key,value in words.items():
        if value > words[m] : m = key
    return m

print(find_longest_word("   amine ben oma a be      hdbfdfdd "))


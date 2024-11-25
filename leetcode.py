def min_max(l):
    i = 0
    while i < len(l) - 1:
        j = 0
        while j < i:
            if l[j] > l[j + 1]:
                l[j],l[j+1] = l[j+ 1], l[j]
            j += 1
        i += 1
    return l[0],l[-1]

# print(min_max([4,5,1,3,8,9]))

def remove_dup(l):
    return list(set(l))

# print(remove_dup([1, 2, 2, 3, 4, 4, 5]))

def second_max(l):
    i = 0
    while i < len(l) - 1:
        j = 0
        while j < i:
            if l[j] > l[j + 1]:
                l[j],l[j+1] = l[j+ 1], l[j]
            j += 1
        i += 1
    return l[-2]

# print(second_max([4,5,1,3,8,9]))

def merge_two_sorted_arrays(l1,l2):
    return list(set(l1 + l2))

# print(merge_two_sorted_arrays([1, 3, 5], [2, 4, 6]))


# Linked Lists: 5. Reverse a singly linked list. 6. Detect if a linked list has a cycle. 7. Find the length of a linked list.


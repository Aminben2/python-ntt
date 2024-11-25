my_list = [1, 2, 3, 4, 5] #tuples , lists and sets are the same in iterating

#The simplest way to iterate through a list
for item in my_list :
    print(item)
print()

# This allows you to loop using the index
for i in range(len(my_list)):
    print(my_list[i])
print()

# This is useful when you need both the index and the value.
for index,value in enumerate(my_list):
    print(f"index : {index}, value : {value}")
print()

# A concise way to iterate and possibly transform elements.
list_names = ["amine","ben","omar"]
print([name.capitalize() for name in list_names])
print()


my_dict = {'a': 1, 'b': 2, 'c': 3}

# a. Iterating over keys
for key in my_dict.keys():
    print("key : {}".format(key))
print()

# b. Iterating over values
for value in my_dict.values():
    print(f"value : {value}")
print()

# c. Iterating over key-value pairs
for key,value in my_dict.items():
    print(f"key : {key}, value : {value}")
print()

# name = "yassine"
# match name:
#     case "amine" :
#         print("ana howa")
#     case "yassine" :
#         print("ana maxi howa")
#     case "ibtissam" :
#         print("ana howa")
#     case _ : print("xkon hada alan")


s = map(lambda x:x**2,my_list)
print(type(s))
print(list(s))
print()

list1=[1,5,8,7]
list2=[78,154,15]
res = map(lambda x,y:x+y,list1,list2)
print(list(res))
print()

s1 = filter(lambda x: x > 2,my_list)
print(type(s1))
print(list(s1))
print()

from functools import reduce
s2 = reduce(lambda x,y: x+y,my_list)
print(s2)
print()

s4 = reduce(lambda x,y: x+y,my_list,20)
print(s4)
print()

s3 = reduce(lambda x,y:x+y,list_names)
print(s3)
print()

# x = 20

# def func():
#     global x
#     x = 50
#     print("inside :",x)
# func()
# print("out side :", x)

"""import decimal

a = decimal.Decimal('1.1')
b = decimal.Decimal('2.2')

c = a+b
print(c)"""

# name ="amine"
# print(f"amine word have {len(name)} characters")
# print(f"amine word have {[5,5,5,5]} characters")

# test = "amine"
# print(test is None,end=" amine")

# print("amine" if 1 > 2 else "ben")
# print("omar" if 5 > 4 else "kan")

# l = [1,2,3,4]
# print(5  in l)
# l.insert(1,"amine")

# print(l)
# if "amine" in l :
#     print(l.index("amine"))  


# print([12,3] + [5, 3])
# l = [12,3]
# l.extend([5, 3])
# print(l)
# print(len(l))

# print(type(()))
# print(type((1)))
# print(type((1,)))

# a,b,c = [1,2,3]
# print(a)
# print(b)
# print(c)

# a,b,c = (1,2,3)
# print(a)
# print(b)
# print(c)


# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# a,b = b,a
# print(a)
# print(b)

a= {}
d = {1:"amine",2:"ben",3:'omar'}

# print(d.get(4,"ibtissam"))
# print(type(d.keys()))

# print(list(d.keys()))

# for i in range(len(d.keys())):
#     print(i)
#     print(d.get(i))


# d.setdefault(1,"kpkp")
# print(d)
# d[3] = "kokp"
# d[4] ="lalala"
# print(d)
# d.update({5:"mememe"})
# print(d)
# del d[5]
# print(d)


# s = set({1,1,1,2,2,3,4})
# ss = {1,2,4,5}

# print(s | ss)
# print(s & ss)

# print({1, 2, 3, 4} - {1,2, 3, 5})

animals_list = ["cat","dog","lion"]

# for animal in animals_list:
#     print(animal)


# for i in range(len(animals_list)):
#     print("index : {} , the animal : {}".format(i,animals_list[i]))

# i = 0
# while i < len(animals_list):
#     print(animals_list[i])
#     i+=1

# for i,value in enumerate(animals_list):
#     print(f"index : {i}, value : {value}")


# love = "i love ibtissam dyaaali"

# i = 0
# while i < len(love):
#     j = 0
#     while j <= i :
#         print(love[j],end="")
#         j += 1
#     print()
#     i +=1

# def ft_print_args(*args):
#     for i in range(len(args)):
#         print(args[i])
# ft_print_args("amine")
# ft_print_args(1,2,54)
# ft_print_args(*(1,2,5))

# def ft_print_keyword_args(**key_args):
#     for key,value in key_args:
#         print(f"key : {key}, value : {value}")

# ft_print_keyword_args(**{"name":"amine","name1":"ibtissam"})

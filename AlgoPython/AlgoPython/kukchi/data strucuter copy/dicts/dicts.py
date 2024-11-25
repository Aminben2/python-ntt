# names = ['yusuf','hamza','hamza','joe','yusuf', 'alex']

# n = dict() 
# for i in names:
# 	n[i] = n.get(i, 0) + 1
# print(n)

# lst1=[]
# lst2=[]
# for k, v in n.items():
# 	lst1.append(k)
# 	lst2.append(v)



# method 2
# m = ['ab','ac','ad','ab', 'ac']
# b = dict()

# for i in m:
# 	if i in b:
# 		b[i] = b[i] + 1
# 	else:
# 		b[i] = 1
# print(b)





d = {}

d["nom"] = "ghizlan"
d.update({"nom1":"Yusuf","nom2":"hamza"})

print(d)

items = d.items()

print(items)
[('nom', 'ghizlan'), ('nom1', 'Yusuf'), ('nom2', 'hamza')]
for i,j in d.items():
	print(i,j)

tup = ()
tup = list(tup)
tup.append("nom")
tup = tuple(tup)
print(tup)


























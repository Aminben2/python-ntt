# chiffre = input("entrer une chiffre: ")
# st = ''
# for i in chiffre:
# 	if i == '0':
# 		st += 'x'
# 		continue
# 	st += i
	
# print(st)
print('*')
for i in range(5):
	print('*', end='')
	for j in range(i+1):
		print("*", end="")
	print()
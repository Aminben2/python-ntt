def Dmatrice(lst):
	for i in lst:
		for j in i:
			print(j, end=" ")
		print()


listGeneral = []
T=int(input("entrer la taille de la liste : "))
Tt=int(input("entrer le nombre de chaque liste: "))
for i in range(T):
	listPetit = []
	for j in range(Tt):
		nb = int(input("entrer les nombre des list: "))
		listPetit.append(nb)
	listGeneral.append(listPetit)


print(Dmatrice(listGeneral))



# for i in range(len(listGeneral)):
# 	for j in range(len(listGeneral[i])):
# 		print(listGeneral[i][j], end=" ")
# 	print()




	
def jeuMot(mot):
	for i in range(len(mot)):
		print('*', end='')
		for j in range(i+1,0,-1): #range(i,-1,-1)
			print(mot[j-1], end="*") # mot[j-1]
		print()

	print()

	for i in range(len(mot)):
		for j in range(i):
			print(" ", end=" ")

		print('*', end='')
		for k in range(i, len(mot)):
			print(mot[k], end="*")
		print()


mot = input("Entrer une mot: ").upper()
jeuMot(mot)


mot = 'salut'.upper()


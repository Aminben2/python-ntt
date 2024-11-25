tab1 = list()
tab2 = list()
n = int(input('Entrer Combien des nombres dans les tableaux: '))

print('1er tableau')
for i in range(n):
	userInput = int(input('Entrer une nombres: '))
	tab1.append(userInput)

print('2eme tableau')
for i in range(n):
	userInput = int(input('Entrer une nombres: '))
	tab2.append(userInput)


if tab1 == tab2:
	print('les tableaux sont identiques')
else:
	print('les tableaux ne sont pas identiques')
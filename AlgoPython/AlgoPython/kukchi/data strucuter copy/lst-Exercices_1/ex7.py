
evenOrOdd = list()

for i in range(int(input('Entrer Combien des nombres: '))):
	userInput = int(input('Entrer une nombres: '))
	evenOrOdd.append(userInput)

even = []
odd = []
for i in evenOrOdd:
	if i % 2 == 0:
		even.append(i)
	else:
		odd.append(i)

print(f'{len(even)} des nombres sont pairs\n{len(odd)} des nombres sont impairs')


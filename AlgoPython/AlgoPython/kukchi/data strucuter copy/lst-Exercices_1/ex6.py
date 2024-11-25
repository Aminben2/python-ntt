n = int(input('Entrer Combien des notes: '))

notes = list()
for i in range(n):
	userInput = int(input('Entrer une note: '))
	notes.append(userInput)
	
print(notes)
counter = 0
for i in notes:
	if i >= 10:
		counter += 1

print(f'{counter} Etudiant ont des notes supérieures à la moyenne')
email = input("entrer votre email: ")

counter = 0

for i in email:
	if i == '@':
		counter += 1

if counter == 0 or counter > 1:
	print('votre email est invalide!')
else:
	print(f"votre email '{email}' est valide!")
	name = ''
	for e in email:
		if e != '@':
			name += e
		elif e == '@':
			break

print(f'Bonjour {name}!')
'''salaireBase = float(input("Entrez votre salaire: "))
if salaireBase < 0:
	print('Donner invalide!')
else:
	catg = input("Entrez votre catégorie: ")

	totalPrime = 0
	if catg != 'a' and catg != 'A' and catg != 'b' and catg != 'B' and catg != 'c' and catg != 'C':
		print("catégoriet invalide!")
	else:
		if catg == 'a' or catg == 'A' :
			totalPrime += 200

		elif catg == 'b' or catg == 'B' :
			totalPrime += 500
			
		elif catg == 'c' or catg == 'C' :
			totalPrime += 700
					
		situation = input("Entrez votre Situation familiale: (m :marié / d :divorcé / v :veuf / c :célibataire) ")

		if situation != "m" and situation != "d" and situation != "v" and situation != "c":
			print("Situation Invalide!")
		elif situation == 'c':
			totalPrime += 0
			print(f"Votre salaire net est {salaireBase + totalPrime}DH")
		else:
			reponse = input("Est ce que tu a des enfants? (oui/non): ")

			if reponse.lower() != "oui" and reponse.lower() != "non" :
				print('reponse invalide!')
			elif reponse.lower() == 'non':
				totalPrime += 0
			else:
				enfant = int(input("Combien des enfants? "))
				if enfant < 0:
					print("Nombre Invalide!")
				else:
					if enfant == 1 :
						totalPrime += 300
					elif enfant == 2 :
						totalPrime += 600
					elif enfant > 2 :
						totalPrime += 1000
						
			print(f"Votre salaire net est {salaireBase + totalPrime}DH")

			


				


'''
'''a,b,c = int(input('a ')),int(input('b ')),int(input('c '))
if a>b and a>c:
	if a**2 == b**2 + c**2:
		print('its a Pythagorean ')
	else:
		print("not a Pythagorean")
elif c>b and c>a:
	if c**2 == a**2 + b**2:
		print('its a Pythagorean ')
	else:
		print("not a Pythagorean")
elif b>c and b>a:
	if b**2 == a**2 + c**2:
		print('its a Pythagorean ')
	else:
		print("not a Pythagorean")


'''
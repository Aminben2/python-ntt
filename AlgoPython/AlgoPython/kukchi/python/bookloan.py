category = input("Entrez votre catégorie(lettre): ")
livres = int(input("Combien des livres voulez-vous emprunter? "))
possession = int(input("Combien d'ouverages à votre possession? "))

totalpossession = possession + livres

if category == 'a' or category == 'A' or category == 'b' or category == 'B' or category == 'c' or category == 'C':
	
	if totalpossession <= 5:
		if category == 'a' or category == 'A': #category.lower()
			print("Vous pouvez emprunter les livres pour une durée de 20 jours")
			possession += livres
		elif category == 'b' or category == 'B':
			print("Vous pouvez q les livres pour une durée de 30 jours")
			possession += livres
		elif category == 'c' or category == 'C':
			print("Vous pouvez emprunter les livres pour une durée de 45 jours")
			possession += livres

	else:
		print("vous ne peuvez pas emprunter un livre")

else:
	print("entrez une valide catégorie!")


a = 0
b = 0

print("\n1. Entrer a et b\n2. Afficher le produit de a et b\n3. Quitter\n")
choix = int(input("Votre Choix: "))
while choix != 3:
	if choix == 1:
		a = int(input("saisir un entier a: "))
		b = int(input("saisir un entier b qui doit etre supérieur strictement à a: "))

		while b < a:
			b = int(input("saisir un entier b qui doit etre supérieur strictement à a: "))
		
	elif choix == 2:
		if a == 0 and b == 0:
			print("Erreur")
			
		else:
			if b-a == 1:
				print("0")
			else:
				P=1
				for i in range(a+1,b):
					P*=i
				print("le produit est", p)

			
	elif choix != 3 and choix > 2:
		print("Erreur")

	print("\n1. Entrer a et b\n2. Afficher le produit de a et b\n3. Quitter\n")
	choix = int(input("Votre Choix: "))

print("Merci")

'''
Algorithme Calculator_cmd
Variables: choix, a, b: entier
Debut
	a <- 0
	b <- 0
	ecrire("\n1. Entrer a et b\n2. Afficher le produit de a et b\n3. Quitter\n")
	ecrire("Votre Choix: ")
	lire(choix)
	tantque choix <> 3 Fair
		si choix == 1 Alors
			ecrire("saisir un entier a:")
			lire(a)
			ecrire("saisir un entier b qui doit etre supérieur strictement à a: ")
			lire(b)
			repeter
				ecrire("saisir un entier b qui doit etre supérieur strictement à a: ")
				lire(b)
			jusqu'a b > a
					
		sinon
			si choix = 2 Alors
				si a = 0 and b = 0:
					ecrire("Erreur")
					
				sinon:
					ecrire(f"le produit de {a} x {b} = {a*b}")
				FinSi
			sinon
				si choix != 3 and choix > 2 Alors
					ecrire("Erreur")
			FinSi
		FinSi

		ecrire("\n1. Entrer a et b\n2. Afficher le produit de a et b\n3. Quitter\n")
		ecrire("Votre Choix: ")
		lire(choix)

	finTantque
	print("Merci")
'''


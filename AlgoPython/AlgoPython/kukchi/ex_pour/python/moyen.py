somme = 0
nombre = 0
i = 1
nbr = float(input(f"entrer le nombre {i}: "))
somme += nbr
if nbr == 0:
	while nbr == 0:
		nbr = float(input(f"entrer le nombre {i}: "))

while nbr != 0:
	i += 1
	nbr = float(input(f"entrer le nombre {i}: "))
	
	if nbr != 0:
		somme += nbr
		nombre +=1
		
print(nombre)
# print(i)
print(f"le moyen est {somme / nombre}")

'''
Algorithme Moyen_with_While
Variables somme, nbr: reel
		  i, nombre : entier
Debut
somme <- 0
nombre <- 0
i <- 1
ecrire("Entrer le nombre numero ", i)
lire(nbr)
somme <- somme + nbr
si nbr = 0 alors
	tantque nbr = 0
		ecrire("Entrer le nombre numero ", i)
		lire(nbr)
	FinTantque
sinon
	tantque nbr <> 0
		i <- i + 1
		ecrire("Entrer le nombre numero ", i)
		lire(nbr)
		si nbr <> 0:
			somme <- somme + nbr
			nombre <- nombre + 1
		FinSi
	FinTantQue
ecrire("le moyen est ", somme / nombre)
'''

'''
Algorithme Moyen_with_DoWhile
Variables somme, nbr: reel
		  i, nombre : entier
Debut
somme <- 0
nombre <- 0
i <- 0
repeter
	i <- i + 1
	ecrire("Entrer le nombre numero ", i)
	lire(nbr)
	si nb <> 0 alors
		somme <- somme + nbr
		nombre <- nombre + 1
	FinSi
	i <- i + 1
jusqu'à nbr = 0

si nb = 0 ET i = 2 alors
	ecrire("Vous avez arretez des le debut")
sinon
	ecrire("le moyen est ", somme / nombre)

'''
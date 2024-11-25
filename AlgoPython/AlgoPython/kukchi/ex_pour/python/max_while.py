# num = int(input("Entrez une nombre: "))
# i = 1
# mx = num
# position = i
# while True:
# 	num = int(input("Entrez une nombre: "))
# 	i += 1
# 	if num == 0:
# 		break
# 	elif num > mx:
# 		mx = num
# 		position = i
		
# print(mx, position)

i = 1
num = int(input(f"Entrez le nombre numero {i} : "))
mx = num
position = i
while num != 0:
	i += 1
	num = int(input(f"Entrez le nombre numero {i} : "))
	if num == 0:
		break
	if num > mx:
		mx = num
		position = i
		
print(mx, position)

"""
algorithm max with while
variable i, position, mx: entier
debut
i <- 1
ecrire("Entrez le nombre numero ," i, ":")
lire(mx)
mx <- num
position <- i
tantque num <> 0:
	i <- i + 1
	ecrire("Entrez le nombre numero ," i, ":")

	si num = 0 alors
		
	si num > mx alors
		mx <- num
		position <- i
		
ecrire(mx, position)

"""


'''
Algortithme max
variables nb, masc: reel
		  i, pmax : entier

Debut
i <- 0
masc <- 0
repeter
	i <- i + 1
	ecrire("Entrer le nombre numero ", i)
	lire(nb)
	si (nb >= masc OU i = 1) ET nb <> 0 alors
		masc <- nb
		pmax <- i
	FinSi
	i <- i + 1
jusqu'à nb = 0
si nb = 0 ET i = 2 alors
	ecrire("Vous avez arretez des le debut")
sinon
	ecrire("le max est", masc, "sa position est ", pmax)
FinSi
Fin



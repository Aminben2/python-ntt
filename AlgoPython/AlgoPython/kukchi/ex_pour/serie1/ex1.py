'''Algorithme sommeXi
Variable: 
		x, somme: reel
		i, n: entier
Debut
ecrire("entrer la valeur de X")
lire(x)
repeter
	ecrire("entrer le nombre d'iteration")
	lire(n)
jusqu'à n > 0
	
somme <- 0
pour i allant de 1 à n
	somme <- somme + (x)^i
ecrire("la somme est ", somme)
'''

n = int(input("entrer le nombre d'iteration: "))
x = float(input("entrer la valeur de X: "))
somme = 0
for i in range(1, n+1):
	somme += x**i
print("la somme est", somme)
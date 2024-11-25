'''Algorithme SigmaXi
Variable: 
	x, sigma: reel
	i, n: entier
Debut
	ecrire("entrer la valeur de X: ")
	lire(x)
	Repeter 
		ecrire("entrer la valeur finale: ")
		lire(n)
	Jusqu'a n > 0
	sigma <- 0
	pour i allant de 1 à n
		sigma <- sigma + (x)^i
	ecrire("la somme est ", sigma)
Fin
'''

n = int(input("Entrez al valeur finale: "))
x = float(input("Entrer la valeur de X: "))
while n < 1:
    n = int(input("Entrez la valeur finale: "))
sigma = 0
for i in range(1, n+1):
    sigma += x**i
print(f"la somme est: {sigma}")

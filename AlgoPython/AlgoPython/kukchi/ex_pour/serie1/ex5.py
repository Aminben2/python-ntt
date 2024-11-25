n = int(input("entrer un nombre: "))
counter = 0
print("entrer 10 nombres: ")
for i in range(10):
	nb = int(input())
	if n == nb:
		counter += 1
print(f"la valeur à rechercher apparait {counter} fois")

'''
Algorithme Recherche_count
variables n, counter, n, i: entier
Debut
	ecrire("entrer un nombre: ")
	lire(n)
	counter <- 0
	ecrire("entrer 10 nombres: ")
	pour i allant de 1 à 10 fair
		lire(nb)
		si n = nb alors
			counter <- counter + 1
	ecrire("la valeur à rechercher apparait ", counter ,"fois")	
'''
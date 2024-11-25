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
	Ecrire("entrer un nombre: ")
	Lire(n)
	Counter <-- 0
	Ecrire("entrer 10 nombres: ")
	Pour i allant de 1 à 10 faire
		lire(nb)
		si n = nb alors
			counter <-- counter + 1
	ecrire("la valeur à rechercher apparait ", counter ,"fois")	
Fin
'''

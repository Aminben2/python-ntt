'''Algorithme lettre_caché
Constante car: "h"
Debut
	Ecrire("Entrez la lettre caché")
	Lire(CAR)
	Tantque CAR <> car
		Si code(CAR) < code(car)
			Ecrire("C'est moins")
			Ecrire("Entrez la lettre caché")
			Lire(CAR)
		Sinon
			Ecrire("C'est plus")
			Ecrire("Entrez la lettre caché")
			Lire(CAR)
		FinSi
    Sinon
		Ecrire("Braavo!")
	FinTanque
Fin
'''
from random import randint 
car = randint(1,10)
# print(car)
CAR = int(input("Entrez la lettre caché: "))
tries = 1
while CAR != car:
	if (CAR) < (car):
		print("C'est moins")
		CAR = int(input("Entrez la lettre caché: "))
	else:
		print("C'est plus")
		CAR = int(input("Entrez la lettre caché: "))
	tries += 1
	
else:
	print(f"Braavo! {tries} ")

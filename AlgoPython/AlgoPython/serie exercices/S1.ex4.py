'''
Algorithme lettre_caché
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

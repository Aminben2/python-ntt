Algorithme; Année bissextile

variables;	year: entier

Début
écrire("Entrez l'année: ")
lire(year)

si (year % 4 = 0) et (year % 100 <> 0) ou (year % 400 = 0) Alors:
	écrire("C'est une année bissextile!")
sinon:
	écrire("ce n'est pas une année bissextile!")
FinSi
Fin

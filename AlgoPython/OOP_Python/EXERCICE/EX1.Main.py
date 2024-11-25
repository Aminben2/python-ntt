from EX1 import Point

A = Point(20, 30)

Bx = int(input("Entrez l'abscisse: "))
By = int(input("Entrez l'Ordonné: "))

B = Point(Bx, By)
B.afficher()
B.deplacer(5, 9)
B.afficher()

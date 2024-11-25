#EXERCICE 1
print("EXERCICE1")
a = float(input("entrez le nombre a"))
b = float(input("entrez le nombre b"))
addition = a+b
print("l'adittion est :", addition)
soustraction = a-b
print("la soustraction est:", soustraction)
produit = a*b
print("le produit est:", produit)
division = a/b
print("la divion est:", division)
modulo = a%b
print("le modulo est:", modulo)
#EXERCICE 2
print("EXERCICE2")
r = float(input("entrez la valeur du rayon"))
pi = 3.14
Surface = (pi)*(r**2)
print("la surface du cercle est:", Surface)
#EXERCICE 3
print("EXERCICE3")
x = float(input("entrez la valeur de x"))
y = 1/(x+1)/(x+1/(x+1/x))))
print("la résultat de y est :", y)
#EXERCICE 4
print("EXERCICE4")
PHT = float(input("entrez le prix HT d'un article"))
NA = int(input("entrez le nombre d'article"))
TTVA = float(input("entrez le taux TVA"))
PTTC = (PHT*NA)*(1+TTVA)
print("Le prix total TTC set:", PTTC)
#EXERCICE 5
print("EXERCICE5")
A = float(input("entrez le premier nombre A"))
B = float(input("entrez le deuxième nombre B"))
import math
print("le carré de A est:", A**2)
print("le carré de B est:", B**2)
print("le résultat de A à la puissance B est:", A**B)
sin = math.sin(A)
cos = math.cos(A)
print("La tangente de A est:", sin/cos)
#EXERCICE 6
print("EXERCICE6")
A = 5.00
B = 2.50
C = 3.00
D = 10.00
E = 7.00
TTVA = 0.20
x= int(input("entrez la quantite du produit A:"))
y= int(input("entrez la quantite du produit B:"))
z= int(input("entrez la quantite du produit C:"))
t= int(input("entrez la quantite du produit D:"))
u= int(input("entrez la quantite du produit E:"))
PHT = x*A+y*B+z*C+t*D+u*E
TVA = PHT*TTVA
PTTC = PHT+TVA
print("Le prix hors taxe de cette vente est:", PHT , "DH")
print("La taxe sur la valeur ajoutée TVA est:", TVA , "DH")
print("Le prix toutes taxes comprises de cette vente est:", PTTC , "DH")







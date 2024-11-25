#Exercice 1
print("Exercice 1")
a = float(input("Entrer le premier nombre"))
b = float(input("Entrer le deuxieme nombre"))
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a mod b =", a % b)

#Exercice 2
print("Exercice 2")
import math
print("Entrer le rayon:")
r=float(input())
print("La surface de cercle est:",r**2*math.pi)

#Exercice 3
print("Enter la valeur de X")
x = float(input())
print("Y = ", 1/(x + (1/(x + 1 / (x +(1/x))))))
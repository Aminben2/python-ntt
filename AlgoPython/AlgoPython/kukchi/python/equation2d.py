from math import pow, sqrt

a = float(input("Entrez la valeur de a: "))
b = float(input("Entrez la valeur de b: "))
c = float(input("Entrez la valeur de c: "))

d = pow(b,2) - (4*a*c)
#print(f"delta = {d}")

if a == 0:
	if b == 0:
		print("Impossible")
	else:
		print(f"Le solution d'equation est {-c/b}")

elif d > 0:
	x1 = (-b-sqrt(d))/(2*a)
	x2 = (-b+sqrt(d))/(2*a)
	print(f"La solution est x1 = {(x1):.3f} et x2 = {(x2):.3f}")
elif d == 0:
	x = -b/(2*a)
	print(f"La solution est x = {x:.3f} ")
else:
	print("N'est pas de solution")


#exercice 1

a=float(input("entrez la valeur de a: "))
b=float(input("ENTREZ LA VALEUR DE B: "))
print(f'la somme est: {a+b}\nla soustraction est: {a-b}\nla multiplication est: {a*b}\nla division est: {a/b}\nle reste de division est: {a%b}\n')

#exercice 2
pi=3.14
r=float(input("entrez le rayon de cercle: "))
print(f"le surface de cercle est :{pi*(r**2)}")

#exercice 3
x = float(input("Entrez la valeur de X: "))
y = 1/(x+1/(x+1/(x+1/x)))
print("{0:.3f}".format(y))


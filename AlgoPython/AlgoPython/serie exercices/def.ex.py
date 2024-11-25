# Example 1
"""
def identification(prenom, age):
    print("Bonjour", prenom, end=" ")
    if age < 0 or age >= 100:
        print("Age invalide")
    elif age < 20:
        print("Vous etes majeur")
    else:
        print("Vous etes majeur")
p = input("Entrez votre prenom: ")
a = int(input("Entrez votre age: "))
# appel en utilisant les arguments de position (positional argument)
# identification(p, a)
# Appel en utilisant les arguments mo clés (keyword arguments)
identification(age=a, prenom=p)
"""

# Example 2
"""
def calcul(a, b, c, d):
    print(f"{a}+{b}+{c}+{d}={a+b+c+d}")
calcul(5, 6, 5, 6)
"""

# Example 3:
"""
def calcul(a, b, c=10):
    print(f"{a}+{b}+{c}={a+b+c}")
calcul(5, 6)
"""

# Example 4: global local example
"""
def example(a):
    i = a
    print("Durant la fonction", i)
i = 5
print("Avant la fonction", i)
example(8)
print("Aprés la fonction", i)
"""

# Exapmle 5:
"""
def glob(a):
    global i
    i = 9
    print("Durant la fonction", i)
i = 5
print("Avant la fonction", i)
glob(8)
print("Aprés la fonction", i)
"""

# Exercice 1:

"""
def gen_pyramid(a):
    for i in range(a+1):
        for j in range(a-i):
            print(" ", end=" ")
        for j in range(1, 2*i):
            print("*", end=" ")
        print()
while True:
    Nb = int(input("Entrez le nombre de ligne: "))
    if Nb == 0:
        break
    else:
        print(gen_pyramid(Nb))
"""

# Exrcice 2:

"""
def date(j, m, a):
    if (a < 0 or j < 0 or m > 12) or (m < 0) or (m == 2 and (j > 29)) or (j > 31 and (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12)) or (j > 30 and (m == 4 or m == 6 or m == 9 or m == 11)):
        print("Date Incorrecte")
    else:
        print("Date correcte")


Jour = int(input("Entrez le jour: "))
Mois = int(input("Entrez le Mois: "))
Année = int(input("Entrez le Année: "))
print(date(Jour, Mois, Année))
"""

# Exdrcice 3:


def bonheur(Nb):
    a = Nb//100
    b = (Nb % 100)//10
    c = (Nb % 100) % 10


A = int(input("entrez: "))
print(bonheur(A))

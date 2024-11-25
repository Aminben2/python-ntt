# ---- 1
def pair(a, b, c):
    a = int(input("Entrez le premier nombre: "))
    b = int(input("Entrez le deuxiéme  nombre: "))
    b = int(input("Entrez le troisieme nombre: "))
    if a % 2 == 0:
        a = a / b
    else:
        a = a * c


"""
FONCTION pair(a:entier,b:entier,c:entier):entier
    variable: a,b,c:entier
    Debut 
        Ecrire("Entrez le premier nombre")
        lire(a)
        Ecrire("Entrez le deuziéme nombre")
        lire(b)
        Ecrire("Entrez le troisiéme nombre")
        lire(c)
        Si i%2=0 Alors
            a = a / b
        Sinon
            a = a * c
        FinSi
    Fin
FinFONCTION
"""
# ---- 2
N = []
NB = int(input("Entrez le nombre des élement: "))

for i in range(NB):
    ele = int(input(f"Entrez l'élement numero {i+1}:"))
    N.append(ele)

NewN = sorted(N)


print(f"La valeur minimale du tableau: {NewN[0]}")
print(f"La valeur maximale du tableau: {NewN[-1]}")
print(f"Le tableau: ")

n = int(input("Entrer un nombre: "))
sumn = 0
for i in range(1,n):
    if n % i == 0:
        sumn += i
if sumn == n:
    print(f"{n} est un nombre parfait")
else:
    print(f"{n} n'est pas un nombre parfait")

'''
Algorithme perfect_number
variables n, sumn, i: entier
Debut
    ecrire("entrer un nombre: ")
    lire(n)
    sumn <- 0
    pour i allant de 1 à n
        si n % i = 0 Alors
            sumn <- sumn + i
        FinSi
    si sumn = n alors
        ecrire(n, "est un nombre parfait")
    sinon
        ecrire(n, "n'est pas un nombre parfait")
    FinSi
Fin
'''

'''
def perfect_number(n):
    sumn = 0
    for i in range(1,n):
        if n % i == 0:
            sumn += i
    if sumn == n:
        print(f"{n} est un nombre parfait")
    # else:
    #     print(f"{n} n'est pas un nombre parfait")

for i in range(10000):
    perfect_number(i)

'''
armstrong
fibonacci


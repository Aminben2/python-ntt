Nb = float(input("Entrez le nombre: "))
max = Nb
pos = 1
i = 1
while Nb == 0:
    Nb = float(input(">Entrez un autre nombre: "))
while Nb != 0:
    i += 1
    Nb = float(input(f"Entrez le nombre numer {i}: "))
    if Nb == 0:
        break
    elif Nb >= max:
        max = Nb
        pos = i
print(f"{max} c'est le plus grand nombre est sa position est: {pos}")

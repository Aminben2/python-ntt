i = 1
Nb = float(input(f"Entrez le nombre numero {i}: "))
somme = Nb
c = 0
while Nb != 0:
    i = i + 1
    Nb = float(input(f"Entrez un nombre numero {i}: "))
    somme += Nb
    c += 1
if Nb == 0 and c == 0:
    print("vous n'avez pas commencer")
else:
    print(f"la moyen est: {somme/c}")

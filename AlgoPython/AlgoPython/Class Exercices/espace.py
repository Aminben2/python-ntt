chaine = input("Ecrire une phrase: ")
Nb = 0
for i in chaine:
    if i == " ":
        Nb += 1
print(f"Il Existe {Nb} espaces")

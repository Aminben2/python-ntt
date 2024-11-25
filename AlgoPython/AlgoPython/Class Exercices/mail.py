mail = input("Entrez votre e-mail: ")
Nb = 0
for i in mail:
    if i == "@":
        Nb += 1
if Nb == 1:
    print("E-mail valide")
    for i in mail:
        if i == "@":
            break
        else:
            print(i, end='')
else:
    print("E-mail invalide")

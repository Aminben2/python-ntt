chaine = input("Ecrire des chifre: ")
for i in chaine:
    if i == "0":
        print("x", end="")
        continue
    print(i, end="")

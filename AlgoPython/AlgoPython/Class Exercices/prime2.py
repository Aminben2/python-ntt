"""
salaireBase = float(input("Entrez votre salaire: "))
cat = input("Entrez votre categorie: ")
if cat == "a" or cat == "A":
    totalPrime = 200
elif cat == "b" or cat == "B":
    totalPrime = 500
elif cat == "c" or cat == "C":
    totalPrime = 700
else: 
    print("Entrez une categorie valide")

SF = input("Entrez votre situation familial: ")
if SF == "célibatire" or SF == "Célibataire":
    print(f"Votre salairenet est: {salaireBase + totalPrime}")
else: 
    enfant = input("Est ce que tu as des enfant?: ")
    if enfant == "OUI" or enfant == "Oui" or enfant == "oui":
        NE = int(input("Combien des enfant vous avez?: "))
        if NE == 1:
            totalPrime = totalPrime + 300
        elif NE == 2:
            totalPrime = totalPrime + 600
        elif NE > 2:
            totalPrime = totalPrime + 1000
print(f"Votre salaire net est: {salaireBase + totalPrime}")
"""
salaireBase = float(input("Entrez votre salaire: "))
if salaireBase <= 0:
    print("Salaire invalide")
else:
    cat = input("Entrez la categorie: ")
    if cat != "A" and cat != "a" and cat != "B" and cat != "b" and cat != "C" and cat != "c" :
        print("Categorie invalide")
    else:
        if cat == "A" or cat == "a":
            salaireBase += 200
        elif cat == "B" or cat == "b":
            salaireBase += 500
        else:
            salaireBase += 700
        print(f"Votre salaire net est: {salaireBase}")
        SF = input("Entrez la situation familial: C : Célibataire / D : Divorcé / M : Marié(e) / V : Veufe: ")
        if SF!="c" and SF!="C" and SF!="d" and SF!="D" and SF!="M" and SF!="m" and SF!="V" and SF!="v":
            print("La situation familial invalide")
        else:
            rep = input("Est ce que vous avez des enfants?: ")
            if rep!="O" and rep!="o" and rep!="N" and rep!="n":
                print("Reponse invalide")
            else:
                if rep == "N" or rep == "n":
                    salaireBase += 0
                else: 
                    NE = int(input("Combien d'enfant vous avez: "))
                    if NE <= 0:
                        print("Reponse invalide")
                    else:
                        if NE == 1:
                            salaireBase += 300
                        elif NE == 2:
                            salaireBase += 600
                        else:
                            salaireBase += 1000 
                        print(f"Votre salaire net est: {salaireBase}")
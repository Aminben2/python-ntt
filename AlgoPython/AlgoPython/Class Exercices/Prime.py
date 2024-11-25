Salaire = float(input("Entrer leur salaire: "))
Cat = input("Entrez leur categorie: ")
SF = input("Entrez leur situation familiale: ")
if SF == "célibataire" and (Cat == "A" or Cat == "a"):
    Salaire = Salaire + 200
elif SF == "célibataire" and (Cat == "B" or Cat == "b"):
    Salaire = Salaire + 500
elif SF == "célibataire" and (Cat == "C" or Cat == "c"):
    Salaire = Salaire + 700
elif (SF == "Marié" or SF == "Mariée" or SF == "Divorcé" or SF == "Divorcée") and (Cat == "A" or Cat == "a"):
    NE = int(input("Combien y'a t'il des enfants: "))
    if NE == 0:
        Salaire = Salaire
    elif NE == 1:
        Salaire = Salaire + 200 + 300
    elif NE == 2: 
        Salaire = Salaire + 200 + 600
    elif NE > 2:
        Salaire = Salaire + 200 + 1000
elif (SF == "Marié" or SF == "Mariée" or SF == "Divorcé" or SF == "Divorcée") and (Cat == "B" or Cat == "b"):
    NE = int(input("Combien y'a t'il des enfants: "))
    if NE == 0:
        Salaire = Salaire
    elif NE == 1:
        Salaire = Salaire + 500 + 300
    elif NE == 2: 
        Salaire = Salaire + 500 + 600
    elif NE > 2:
        Salaire = Salaire + 500 + 1000
elif (SF == "Marié" or SF == "Mariée" or SF == "Divorcé" or SF == "Divorcée") and (Cat == "A" or Cat == "a"):
    NE = int(input("Combien y'a t'il des enfants: "))
    if NE == 0:
        Salaire = Salaire
    elif NE == 1:
        Salaire = Salaire + 700 + 300
    elif NE == 2: 
        Salaire = Salaire + 700 + 600
    elif NE > 2:
        Salaire = Salaire + 700 + 1000
print("Leur salaitre net est: ", Salaire)

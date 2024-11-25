#EXERCICE 1
print("exercice 1")
a = int(input("Entrez l'annee:"))
if a<1 :
    print("l'annee invalide")
elif(a%4 ==0 and a%100 !=0) or (a%400 ==0) :
    print("l'annee est bissextile")
else :
    print("l'annee est non bissextile")
#EXERCICE 2
print("exercice 2")
sal = float(input("Entrez votre salaire"))
if sal<500 :
    print("salaire invalide")
elif sal>=12000 :
    print("vous etes aucune prime")
else :
    sf = input("""Entrez votre situation familiale :
            m : marie
            c : célibataire
            d : divorcé
            v : veuf""")
    if sf=="m" :
        print("votre salire est:", (sal+sal*0.2))
    elif sf=="c" :
        print("votre salaire est:", (sal+sal*0.1))
    elif sf=="d" or sf=="v" :
        empd= input("entrez non pour pas d'enfant et oui pour vous avez d'enfant")
        if empd=="non" :
            print("votre salaire est :", sal+(sal*0.1))
        elif empd=="oui" :
            print("votre salaire est :", (sal+sal*0.3))
        else :
            print("nombre d'enfant est  invalide")
    else :
        print("situation familiale est invalide")
################################################
#EXERCICE 3 :
print("EXERCICE 3")
from datetime import date
salaire = float(input("Entrez votre salaire"))
annee1 = int(input("Entrez l'annee de naissance"))
annee2 = int(input("Entrez l'annee de recrutement"))
if s<500 or an<1900 or ar<=an+18 or ar<=an or an>date or ar>date :
    print("date invalide")
age = 2023-annee1
experience = 2023-annee2
if age< 40 and experience >= 10:
    print("la retraite est:", salaire-(0.20*salaire))
elif 40 <= age <= 55 and experience >= 15:
    print("la retraite est :", salaire-(0.10*salaire))
else :
    print("la retraite est :", salaire)
##################################################
#EXERCICE 4:
print("EXERCICE 4")
s = float(input("Entrez votre salaire"))
if s<=500 :
    print("Salaire invalide")
else :
    age = int(input("Entrez l'age"))
    if age<=18 :
        print("Age invalide")
    else :
        g = input("Entrez votre sexe : H=Homme / F=Femme")
        if genre!="H" and genre!="h" and genre!="F" and genre!="f" :
            print("genre invalide")
        elif (genre=="H" or genre=="h") and age>=20 :
            print("l'impot est:", s*0.1)
        elif (genre=="F" or genre=="f") and 18<=age<=35 :
            print("l'impot est:", s*0.07)
        else :
            print("pas  d'impot a payer")




























        

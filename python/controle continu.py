#CONTROLES CONTINUE
print("EXERCICE 4")
prxu = float(input("Entrez le prix unitaire:"))
if prxu<=0 :
    print("Le prix est invalide")
else :
    Q = int(input("Entrez la quantitée achetée:"))
    if Q<=0 :
        print("la quantité est invalide")
    else :
        cat = int(input("Entrez la catégorie du  produit=cat :"))
        if cat<0 :
            print("la catégorie est invalide")
        elif 0<=cat<=1 :
            print("le montant de la taxe est:", prxu*0.06, "et le prix a payer est:", (prxu+(prxu*0.06))*Q)
        elif 1<cat<=3 :
            print("le montant de la taxe est:", prxu*0.09, "et le prix a payer est:", (prxu+(prxu*0.09))*Q)
        elif 4<=cat<=7 :
            print("le montant de la taxe est:", prxu*0.15, "et le prix a payer est:", (prxu+(prxu*0.15))*Q)
        else :
            print("le montant de la taxe est:", prxu*0.2, "et le prix a payer est:", (prxu+(prxu*0.2))*Q)
    
    

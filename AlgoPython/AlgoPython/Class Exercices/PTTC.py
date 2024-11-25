X = int(input( "Entrer le nombre de produit A: "))
Y = int(input( "Entrer le nombre de produit B: "))
Z = int(input( "Entrer le nombre de produit C: "))
T = int(input( "Entrer le nombre de produit D: "))
U = int(input( "Entrer le nombre de produit E: "))
A = 5
B = 2.5
C = 3 
D = 10
E = 7 
PHT = (X * A) + (Y * B) + (Z * C) + (T * D) + (U * E)
print("Le prix hors taxe est: ", PHT)
TVA = PHT * 0.2 
print ("le taux sur la valeur ajoutée est : ",TVA )
PTTC = PHT + TVA 
print(f"le prix toutes taxes comprises est : {PTTC} DHS")



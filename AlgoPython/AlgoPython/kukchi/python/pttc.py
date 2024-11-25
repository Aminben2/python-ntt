Pa=5
Pb=2.5
Pc=3
Pd=10
Pe=7
TTVA=0.20

X=float(input("entrez la quantiter acheter du produit A "))
Y=float(input("entrez la quantiter acheter du produit B "))
Z=float(input("entrez la quantiter acheter du produit C "))
T=float(input("entrez la quantiter acheter du produit D "))
U=float(input("entrez la quantiter acheter du produit E "))

NPA=X+Y+Z+T+U
PHT=(X*Pa)+(Y*Pb)+(Z*Pc)+(T*Pd)+(U*Pe)
TVA=PHT*TTVA
PTTC=PHT*TVA

print(f"le prix hors taxe est {PHT}DHS")
print(f"la taxe sur la valeur ajouter est {TVA}DHS")
print("Le prix toutes taxes comprises",PTTC)

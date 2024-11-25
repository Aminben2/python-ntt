HT = float(input("Entrer le prix HT: "))
NB = float(input("Entrer le nombre d'articles: "))
TVA = float(input("Entrer le TVA: "))/100
TTC = HT * NB * (1 + TVA)
print(f"Le prix total TTC est: {TTC} DHS")


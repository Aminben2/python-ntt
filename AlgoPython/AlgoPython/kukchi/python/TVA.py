prix_ht = float(input("Entrez le prix HT d'article: "))
nb_a = float(input("Entrez le nombre d'articles: "))
tva = float(input("Entrez le taux TVA: "))/100

ttc = prix_ht * nb_a * (1+tva)
print(f"Prix total TTC est {ttc:.2f}DHS")
def totalSales(d):
    totalSalesList = d.values()
    return sum(totalSalesList)


def bestSeller(d):
    topSellingAmount = max(d.values())
    Sellers = d.keys()
    for Seller in Sellers:
        if d[Seller] == topSellingAmount:
            return Seller


def delBadSeller(d):
    lessSellingAmount = min(d.values())
    Sellers = d.keys()
    for Seller in Sellers:
        if d[Seller] == lessSellingAmount:
            lessSellingAmountSeller = Seller
    del d[lessSellingAmountSeller]
    ventes = d
    return ventes


def deleteSeller(name, d):
    del d[name]
    ventes = d
    return ventes


def sortSales(d):
    # Short way
    salesList = sorted([(v, k) for (k, v) in d.items()], reverse=True)
    newDict = dict([(k, v) for (v, k) in salesList])
    return newDict
    # Long way
    # salesList = []
    # for k, v in d.items():
    # 	salesList.append((v, k))
    # salesList = sorted(salesList, reverse=True)

    # newDict = []
    # for v, k in salesList:
    # 	newDict.append((k,v))
    # return dict(newDict)


def salesUpdate(name, d):
    amount = int(input(f'Entrer le nombre de ventes de {name}: '))
    d[name] = amount
    ventes = d
    return ventes


def enregistrer_ventres(d):
    with open("ventes.txt", "w") as ventres:
        for k, v in d.items():
            ventres.write(f"{k} => {v}\n")
    print("Enregistrer dans ventes.txt")


ventes = {"Dupont": 14, "Hervy": 19, "Geoffroy": 15, "Layec": 21, "Yusuf": 11}


MENU = """
-------------Menu-------------
1 : Ajouter les ventes
2 : Afficher les ventes.
3 : Afficher les ventes triées.
4 : Modifier les ventes d’un vendeur .
5 : Rechercher les ventes d’un vendeur .
6 : Supprimer un vendeur .
7 :Afficher le nombre total des ventes
8 :Afficher le vendeur qui a réalisé plus de vente
9 : Enregistrer dans un fichier
10: Quittez le programme
"""

print(MENU.strip())
choice = int(input('Tapez votre choix : '))

while choice < 1 or choice > 10:
    choice = int(input('Tapez votre choix : '))
while True:
    if choice == 2:
        for k, v in ventes.items():
            print(f"-------------\n{k} : {v} Ventes")

    elif choice == 3:
        vente = sortSales(ventes)
        for k, v in vente.items():
            print(f"-------------\n{k} : {v} Ventes")

    elif choice == 4:
        for k, v in ventes.items():
            print(f"{k} : {v} Ventes")
        name = input("Entrer le nom de vendeur : ").capitalize()
        salesUpdate(name, ventes)

    elif choice == 6:
        name = input("Entrer le nom de vendeur : ").capitalize()
        deleteSeller(name, ventes)
    elif choice == 7:
        print(totalSales(ventes))
    elif choice == 8:
        print(bestSeller(ventes))
    elif choice == 9:
        enregistrer_ventres(ventes)
    elif choice == 10:
        print("MERCI!!")
        break
    else:
        choice = int(input('Tapez votre choix : '))

    continu = input('\nContinue? (y/n) ').lower()
    if continu == 'y':
        print(MENU)
        choice = int(input('Tapez votre choix : '))
    else:
        break

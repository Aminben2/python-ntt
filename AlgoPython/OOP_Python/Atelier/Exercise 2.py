class Fournisseur:
    def __init__(self, nf="Moad", ad="Kouilma", c=0):
        self.__nom = nf
        self.__adrs = ad
        self.__code = c

    def getNom(self):
        return self.__nom

    def setNom(self, nom):
        self.__nom = nom

    def getAdresse(self):
        return self.__adrs

    def setAdresse(self, ad):
        self.__adrs = ad

    def getCode(self):
        return self.__code

    def ToString(self):
        return f"Nom Fournisseur: {self.__nom}, Code Fournisseur: {self.__code}, Adresse: {self.__adrs}"

    def Equals(self, F):
        self.__code == F.__code and self.__nom == F.__nom


class produit:
    def __init__(self, ds="jfd", pr=10, fr=Fournisseur()):
        self.__désignation = ds
        self.__prix = pr
        self.__fournisseur = fr

    def getDésignation(self):
        return self.__désignation

    def setDésignation(self, des):
        self.__désignation = des

    def getPrix(self):
        return self.__prix

    def setPrix(self, pr):
        self.__prix = pr

    def getFournisseur(self):
        return self.__fournisseur

    def setFournisseur(self, fr):
        self.__fournisseur = fr

    def ToString(self):
        return f"Désignation: {self.__désignation}, Prix: {self.__prix}, \n Fournisseur: {self.__fournisseur.ToString()}"

    def Equals(self, P1):
        return self.__désignation == P1.__désignation


lst = []
choix = 2
while choix != 5:
    print("""
1- Listes des produits
2- Ajouter un produit
3- Supprimer produit
4- Rechercher produit
5- Quitter Programme
""")

    choix = int(input("Entrez votre choix: "))
    if choix == 1:
        for i in lst:
            print(i.ToString())

    elif choix == 2:
        DES = input("Entrez la désignation: ")
        PR = int(input("Entrez le prix: "))
        NF = input("Entrez nom fournisseur: ")
        AD = input("Entrez l'adresse: ")
        FR = Fournisseur(NF, AD)
        P = produit(DES, PR, FR)
        lst.append(P)

    elif choix == 3:
        sup = input("Entrez la désignation à supprimer: ")
        exist = False
        for i in lst:
            if i.getDésignation() == sup:
                exist = True
                lst.remove(i)
        if not(exist):
            print("Ce produit n'existe pas")

    elif choix == 4:
        rech = input("Entrez le nom à rechercher: ")
        exist = False
        for i in lst:
            if i.getDésignation() == rech:
                i.ToString()
                exist = True
        if not(exist):
            print("Ce produit n'existe pas")

    elif choix == 5:
        print("Fin Programme")

    else:
        ("Choix Invalid")

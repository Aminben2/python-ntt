class client:
    auto = 1

    def __init__(self, nc, ad):
        self.__nom = nc
        self.__code = self.auto
        self.__adresse = ad
        client.auto += 1

    def getNom(self):
        return self.__nom

    def setNom(self, nom):
        self.__nom = nom

    def getAdresse(self):
        return self.__adresse

    def setAdresse(self, ad):
        self.__adresse = ad

    def getCode(self):
        return self.__code

    def ToString(self):
        return f"Nom Client: {self.__nom}, Code Client: {self.__code}, Adresse: {self.__adresse}"

    def Equals(self, C1):
        self.__code == C1.__code and self.__nom == C1.__nom


lst = []
choix = 2
while choix <= 6:
    print("""
    1- Ajouter Client:
    2- Afficher tous les clients
    3- Supprimer Client par son nom
    4- Rechercher un client par son nom
    5- Modifier l'adesse d'un client par so nom
    6- Quitter le programme
    """)
    choix = int(input("Entrez votre choix: "))

    if choix == 1:
        nomC = input("Entrez le nom de client: ")
        adresse = input("Entrez l'adresse de client: ")
        C = client(nomC, adresse)
        lst.append(C)

    elif choix == 2:
        for i in lst:
            print(i.ToString())

    elif choix == 3:
        sup = input("Entrez le nom à supprimer: ")
        exist = False
        for i in lst:
            if i.getNom() == sup:
                exist = True
                lst.remove(i)
        if not(exist):
            print("Ce client n'existe pas")
    elif choix == 4:
        rech = input("Entrez le nom à rechercher: ")
        exist = False
        for i in lst:
            if i.getNom() == rech:
                i.ToString()
                exist = True
        if not(exist):
            print("Ce client n'existe pas")
    elif choix == 5:
        mod = input("Entrez le nom à modifier: ")
        exist = False
        for i in lst:
            if i.getNom() == mod:
                ad = input("Entrez la nouvelle adresse: ")
                nm = input("Entrez le nouveau nom: ")
                i.setNom(nm)
                i.setAdresse(ad)
                exist = True
        if not(exist):
            print("Ce client n'existe pas")
    elif choix == 6:
        print("Fin programme")
    else:
        print("choix invalid")

class personne:
    def __init__(self, cin='0', n='nom', p='prenom', an=0):
        self.__CIN = cin
        self.__Nom = n
        self.__Prenom = p
        self.__ANaiss = an

    def getNom(self):
        return self.__Nom

    def setNom(self, n):
        self.__Nom = n

    def getPrenom(self):
        return self.__Prenom

    def setPreom(self, p):
        self.__Prenom = p

    def getAN(self):
        return self.__ANaiss

    def setAN(self, a):
        self.__ANaiss = a

    def getCIN(self):
        return self.__Nom

    def setCIN(self, c):
        self.__CIN = c

    def afficher(self):
        print(
            f"CIN: {self.__CIN}, Nom: {self.__Nom}, Prenom: {self.__Prenom}, ANaiss: {self.__ANaiss}")

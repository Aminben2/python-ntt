class personne:
    def __init__(self, id=0, n="nom", s=0):  # ------ 4 ------
        self.__Id = id
        self.__Nom = n
        self.__Salaire = s

    def getId(self):  # ------ 2 ------
        return self.__Id

    def setId(self, id):
        self.__Id = id

    def getNom(self):
        return self.__Nom.upper()

    def setNom(self, n):
        self.__Nom = n

    def getSalaire(self):
        return self.__Salaire

    def setsalaire(self, s):
        self.__Salaire = s

    def afficherPersonne(self):
        print(f"Nom: {self.__Nom}, Id: {self.__Id}, Salaire: {self.__Salaire}DH")

    def _afficherPersonne(self):
        print(f"Nom: {self.__Nom}, Id: {self.__Id}, Salaire: {self.__Salaire}DH")


class utilisateur(personne):
    def __init__(self, id=0, n="nom", s=0,  log="fgf", psw="vl"):
        self.__Login = log
        self.__Password = psw
        super().__init__(id, n, s)

    def getLogin(self):
        return self.__Login

    def setLogin(self, L):
        self.__Login = L

    def getPassword(self):
        return self.__Password

    def setPassword(self, psw):
        self.__Password = psw

    def afficherUtilisateur(self):
        self.afficherPersonne()
        print(f"Login: {self.__Login}, Password: {self.__Password}.")


# lst = []
# nb = int(input("Utilisateur ?: "))
# for i in range(nb):
#     nom = input("Entrez le nom: ")
#     id = int(input("Entrez l'ID: "))
#     salaire = input("Entrez le salaire: ")
#     log = input("Entrez votre mail: ")
#     psw = input("Entrez le password: ")
#     U = utilisateur(log, psw, id, nom, salaire)
# lst.append(U)

U1 = utilisateur(45, "moad", 2500, "lfoigf", "kdbor")
U2 = utilisateur(45, "ayman", 3000, "mlkjh", "iyfliy")
U3 = utilisateur(45, "manal", 3500, "menbv", "ykryr")

lst_U = [U1, U2, U3]
login = input("Entrez votre login: ")
mdp = input("Entrez votre mot de passe: ")
for i in lst_U:
    existe = False
    if i.getLogin() == login and i.getPassword() == mdp:
        existe = True
        break

if existe == True:
    print("Authentification reussie: Bienvenue")
    i.afficherUtilisateur()
else:
    print("Authentification echouer")

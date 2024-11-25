from datetime import date
from abc import ABCMeta, abstractmethod


class client:
    num = 0

    def __init__(self, n="ljvjl", p="gcluc"):
        self.__numclient = client.num
        self.__nom = n
        self.__prenom = p
        client.num += 1

    def getNom(self):
        return self.__nom

    def setNom(self, n):
        self.__nom = n

    def getPrenom(self):
        return self.__prenom

    def setPreom(self, p):
        self.__prenom = p

    def getNumC(self):
        return self.__numclient

    NumC = property(getNumC)
    NomC = property(getNom, setNom)
    PrenomC = property(getPrenom, setPreom)

    def __str__(self):
        return f"Prénom: {self.Nom}, Nom: {self.Prenom}, Numero client: {self.NumC}"

    def equals(self, F):
        return self.__numclient == F.__numclient


class Facture(metaclass=ABCMeta):
    def __init__(self, nf=65, mntfac=6565, c=client(), d=date.today()):
        self._NumF = nf
        self._Mantant = mntfac
        self._client = c
        self._date = d

    def getNumF(self):
        return self._NumF

    def setNumF(self, N):
        self._NumF = N

    def getClient(self):
        return self._client

    def setClient(self, C):
        self._client = C

    def getMantant(self):
        return self._Mantant

    def setMantant(self, M):
        if M >= 0:
            self._Mantant = M
        else:
            print("Error")

    def getDate(self):
        return self._date

    def setDate(self, DF):
        if DF < date.today():
            self._date = DF
        else:
            print("Error")

    NumF = property(getNumF, setNumF)
    mnt = property(getMantant, setMantant)
    clt = property(getClient, setClient)
    datef = property(getDate, setDate)

    @abstractmethod
    def getRemise(self):
        pass

    def GetAncienneteFacture(self):
        return f"L'ancienneté de la facture est: {date.today().year - self.datef.yaer} ans."

    def __str__(self) -> str:
        return f"Nom: {self._NumF}, Montant: {self._Mantant}, Client: {self._}"


class FactureLocale(Facture):
    def __init__(self, nf=45, mnt=6565, c=client(), d=date(1999, 1, 1), v="gfd"):
        super().__init__(nf, mnt, c, d)
        self.__ville = v

    @property
    def ville(self):
        return self.__ville

    @ville.setter
    def ville(self, v):
        self.__ville = v

    # ville = property(getVille, setVille)
    def getRemise(self):
        remise = 0
        if self._Mantant > 200:
            remise = self._Mantant * 0.1
        return remise


class FactureEtranger(Facture):
    def __init__(self, nf=65, mntfac=6565, c=client(), d=date.today(), nu=48, p="pays"):
        super().__init__(nf, mntfac, c, d, nu)
        self.__pays = p

    def getPays(self):
        return self.__pays

    def setPays(self, p):
        self.__pays = p

    pays = property()

    def getRemise(self):
        remise = 0
        if self._Mantant > 100:
            remise = self._Mantant * 0.15
        return remise

    def __add__(self, F1):
        f = FactureEtranger()
        f.mnt = self.mnt + F1.mnt
        return f

    def __str__(self) -> str:
        return f"{super().__str__()}, Ville: {self}"


class listFacture:
    def __init__(self, f=[]):
        self.__L_facture = f

    @property
    def LF(self):
        return self.__L_facture

    @LF.setter
    def LF(self, L):
        self.__L_facture = L

    def ajouter(self, F):
        if F in self.__L_facture:
            print("La facture existe")
        else:
            self.__L_facture.append(F)

    def Ajouter(self, NumF):
        exist = False
        for i in self.__L_facture:
            if i.numf == NumF:
                exist = True
                break
        if exist:
            print("Cette facture existe deja")
        else:
            natureF = input('Facture locale: L / Facture etranger: E')
            if natureF == "L":
                FL = FactureLocale(v=input('Entrez la ville: '))
                self.__L_facture.append(FL)
            elif natureF == "E":
                FE = FactureEtranger(p=input("Entrez le pays: "))
                self.__L_facture.append(FE)
            else:
                print("Nature du facture invalide")

    def Supprimer(self, numF):
        exist = False
        for i in self.__L_facture:
            if i.numf == numF:
                exist = True
                self.__L_facture.remove(i)
                break
        if not (exist):
            print("cette facture n'existe pas!")

    def ListeFactureClient(self, numc):
        LFC = []
        for i in self.__L_facture:
            if i.clt.Numc == numc:
                LFC.append(i)
        return LFC

    def listefacturelocal(self):
        fl = []
        for i in self.__L_facture:
            if isinstance(i, FactureEtranger) == True:
                fl.append(i)
        return fl

    def listefactureetranger(self):
        fe = []
        for i in self.__l_factures:
            if isinstance(i, FactureEtranger) == True:
                fe.append(i)
        return fe


v = client("moad", "boujamaa")

print(isinstance(v, client))
print(isinstance(v, Facture))

from abc import ABCMeta, abstractmethod
from datetime import date
from logging import exception

"""
class date:
    def __init__(self,y,m,d):
        self.year=y
        self.month=m
        self.day=d

    def __str__(self):
        return f"{self.year}---{self.month}--{self.year}"

    @staticmethod
    def today(self):
        return f" {self.yeartoday} -- {monthtoday} -- {daytoday}"
"""


class client:
    auto = 0

    def __init__(self, n="nom", p="prenom"):
        self.__nom = n
        self.__prenom = p
        client.auto += 1
        self.__num = client.auto

    def getNom(self):
        return self.__nom

    def setNom(self, n):
        self.__nom = n

    def getprenom(self):
        return self.__prenom

    def setprenom(self, p):
        self.__prenom = p

    def getNum(self):
        return self.__num

    nom = property(getNom, setNom)
    prenom = property(getprenom, setprenom)
    num = property(getNum)

    def __str__(self):
        return f" le numero de client est  : {self.__num}---- le nom est {self.__nom} ---- le prenom est {self.__prenom} "

    def equals(self, c1):
        if self.__num == c1.__num:
            return True
        else:
            return False


class MntExc(exception):
    def __str__(self):
        return "Montant doit étre supperieur à 0"


class DateExc(exception):
    def __str__(self):
        return "Date ne doit pas deppasser la date d'aujourdhui"


class facture(metaclass=ABCMeta):
    def __init__(self, num=0, mnt=0, df=date(2000, 1, 1), c=client()):
        self._numero = num
        self._montant = mnt
        self._dat = df
        self._client = c

    def getNum(self):
        return self._numero

    def setNum(self, num):
        self._numero = num

    def getmontant(self):
        return self._montant

    def setmontant(self, mnt):
        if mnt >= 0:
            self._montant = mnt
        else:
            raise MntExc()

        # if mnt<=0:
        #     print("impossible ")
        # else:
        #     self._montant=mnt

    def getDate(self):
        return self._dat

    def setDate(self, d):
        if d > date.today():
            print("impossible")
        else:
            self._dat = d

    def getclient(self):
        return self._client

    def setclient(self, c):
        self._client = c

    numf = property(getNum, setNum)
    montantf = property(getmontant, setmontant)
    datef = property(getDate, setDate)
    client = property(getclient, setclient)

    @abstractmethod
    def getRemise(self):
        pass

    def getAncienneFacture(self):
        return date.today().year - self._dat.year


class FactureLocale(facture):
    def __init__(self, num=0, mnt=200, df=date(2000, 1, 1), c=client(), v="ville"):
        super().__init__(num, mnt, df, c)
        self.__ville = v

    def getVille(self):
        return self.__ville

    def setville(self, v):
        self.__ville = v

    vi = property(getVille, setville)

    def getRemise(self):
        if self._montant < 200:
            return 0
        else:
            return self.getmontant()*(10/100)


class factureEtranger(facture):
    def __init__(self, num=0, mnt=200, df=date(2000, 1, 1), c=client(), p="pays"):

        self.__pays = p
        super().__init__(num, mnt, df, c)

    def getp(self):
        return self.__pays

    def setp(self, p):
        self.__pays = p

    pays = property(getp, setp)

    def getRemise(self):
        if self._montant < 100:
            return 0
        else:
            return self.getmontant()*0.15

    def __add__(self, FE):
        f1 = factureEtranger()

        f1.mnt = self.mnt+FE.mnt
        return f1


class ListeFacture:
    def __init__(self, Lf=[]):
        self.__listef = Lf

    def getlitsef(self):
        self.__listef

    def setlistef(self, lf):
        self.__listef = lf

    @property
    def LF(self):
        return self.__listef

    @LF.setter
    def LF(self, l):
        self.__listef = l

    def ajouterfacture(self, c):
        if c in self.__listef:
            print("facture deja existante:")
        else:
            self.__listef.append(c)

    def Ajouterfn(self, numfa):
        exist = False

        for i in self.__listef:
            if i.numf == numfa:
                existe = True
                break
        if exist == True:
            print("la facture exist deja:")
        else:
            natureF = input("Facture Locale ou facture Etrangere ")
            if natureF == "L":
                FL = FactureLocale(v=input("entrez la ville:"))
                self.__listef.append(FL)
            elif natureF == "E":
                FE = factureEtranger(p=input("entrez le pays:"))
                self.__listef.append(FE)
            else:
                print("nature de facture invalide:")

    def supprimer(self, n):
        Existe = False
        for i in self.__listef:
            if i.numf == n:
                Existe = True
                break
        if Existe:
            self.__listef.remove(i)

    def listeFacture(self, numc):
        lfc = []
        for i in self.__listef:
            if i.client.num == numc:
                lfc.append(i)
        return lfc
# i.client(hya propriete li seminaha f facture ////  i.client.num : num de facture li f client

    def listeFactureLocal(self):
        lfl = []
        for i in self.__listef:
            if isinstance(i, FactureLocale) == True:
                lfl.append(i)
        return lfl

    def listeFactureEtranger(self):
        lfe = []
        for i in self.__listef:
            if isinstance(i, factureEtranger) == True:
                lfe.append(i)
                """
                if hasattr(i,__pays):
                    FE.append(i)
                """
        return lfe


'''      
f=facture()
f.datef=date(1994,11,1)
print(f.datef)
f.montantf=6576
print(f.montantf)
'''
ff = FactureLocale()
print(ff.getRemise())
# print(f.getAncienneFacture())

fe = factureEtranger()
print(fe.getRemise())


#print((date.today().year - date(1994,11,1).year))

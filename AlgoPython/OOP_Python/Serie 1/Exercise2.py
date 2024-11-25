class Zone:
    def __init__(self, id=1, nz='tetouan'):
        self.__idZone = id
        self.__NomZone = nz

    def getIdZone(self):
        return self.__idZone

    def setIdZone(self, z):
        self.__idZone = z

    def getNomZone(self):
        return self.__NomZone

    def setNomZone(self, z):
        self.__NomZone = z


class Pays:
    def __init__(self, ip=0, np='maroc', z=Zone()):
        self.__ipPays = ip
        self.__NomPays = np
        self.__zone = z

    def getIdPay(self):
        return self.__ipPays

    def setIdPay(self, z):
        self.__NomPays = z

    def getNomPay(self):
        return self.__NomPays

    def setNomPay(self, z):
        self.__NomPays = z

    def getZone(self):
        return self.__zone

    def setZone(self, z):
        self.__zone = z


class Ville:
    def __init__(self, id=1, Nv='ff', cp=93000, p=Pays()):
        self.__idVille = id
        self.__NomVille = Nv
        self.__CodePostal = cp
        self.__Pays = p

    def getidville(self):
        return self.__idVille

    def setidville(self, z):
        self.__idVille = z

    def getNomVille(self):
        return self.__NomVille

    def setNomVille(self, z):
        self.__NomVille = z

    def getCode(self):
        return self.__CodePostal

    def setCode(self, z):
        self.__CodePostal = z

    def getPays(self):
        return self.__Pays

    def setPays(self, z):
        self.__Pays = z


class Catégorie:
    def __init__(self, id=2, nc='ccc'):
        self.__idCatégorie = id
        self.__NomCatégorie = nc

    def getIdCat(self):
        return self.__idCatégorie

    def setIdCat(self, i):
        self.__idCatégorie = i

    def getNomCat(self):
        return self.__NomCatégorie

    def setNomCat(self, nc):
        self.__NomCatégorie = nc


class Produit:
    def __init__(self, id=15, np='pro', pp=12.6, c=Catégorie()):
        self.__idProduit = id
        self.__NomProduit = np
        self.__PrixProduit = pp
        self.__catégorie = c

    def getIdProduit(self):
        return self.__idProduit

    def setIdProduit(self, z):
        self.__idProduit = z

    def getNomPro(self):
        return self.__NomProduit

    def setNomPro(self, z):
        self.__NomProduit = z

    def getPrix(self):
        return self.__PrixProduit

    def setPrix(self, z):
        self.__PrixProduit = z

    def getCatégorie(self):
        return self.__catégorie

    def setCatégorie(self, z):
        self.__catégorie = z

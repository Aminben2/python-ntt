from abc import ABC, abstractmethod


@abstractmethod
class imprimable(ABC):
    def imprimer(self):
        pass


class Article(imprimable):
    def __init__(self, n="", nb=45):
        self.__NomA = n
        self.__nombreP = nb

    @property
    def NomA(self):
        return self.__NomA

    def nombreP(self):
        return self.__nombreP

    @NomA.setter
    def NomA(self, n):
        self.__NomA = n

    @nombreP.setter
    def NbPage(self, p):
        self.__nombreP = p

    def imprimer(self):
        return f"{self.NomA} est un Article imprimable sur {self.nombreP} pages"


class Magazine(imprimable):
    def __init__(self, nm="kjdf", nb=45):
        self.__nomMagazine = nm
        self.__nombrePage = nb

    @property
    def nomMagazine(self):
        return self.__nomMagazine

    def nombrePage(self):
        return self.__nombrePage

    @nomMagazine.setter
    def nomMagazine(self, dk):
        self.__nomMagazine = dk

    @nombrePage.setter
    def nombrePage(self, hf):
        self.__nombrePage = hf

    def imprimer(self):
        return f"{self.nomMagazine} est un Magazine imprimable {self.nombrePage}"

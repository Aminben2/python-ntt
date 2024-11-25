from abc import ABC, abstractmethod


class Imprimer(ABC):
    @abstractmethod
    def Imprimer(self):
        pass


class Article(Imprimer):
    def __init__(self, nomA="nom article", np=0):
        self.__nomA = nomA
        self.__np = np

    @property
    def nomA(self):
        return self.__nomA

    @nomA.setter
    def nomA(self, n):
        self.__nomA = n

    @property
    def np(self):
        return self.__np

    @np.setter
    def np(self, np):
        self.__np = np

    def Imprimer(self):
        print(f"nom d'article: {self.nomA}, nombre des pages: {self.np}")


class Magazin (Imprimer):
    def __init__(self, nomM="nom magazin", npM=0):
        self.__nomM = nomM
        self.__npM = npM

    @property
    def nomM(self):
        return self.__nomM

    @nomM.setter
    def nomM(self, nm):
        self.__nomM = nm

    @property
    def npM(self):
        return self.__npM

    @npM.setter
    def npM(self, npM):
        self.__npM = npM

    def Imprimer(self):
        print(f"nom d'Magazine: {self.nomM}, nombre des pages: {self.npM}")


a1 = Article("hicham", 155)
a1.Imprimer()

m1 = Magazin("ahmed", 239)
m1.Imprimer()

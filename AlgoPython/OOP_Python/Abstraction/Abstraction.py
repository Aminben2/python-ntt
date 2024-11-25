# Class Abstraite
import math


class Forme:
    def __init__(self, n="nom"):
        self.__nom = n

    def Surface(self):
        pass

    def Perimetre(self):
        pass


class Rectangle(Forme):
    def __init__(self, n="nom", l=0, L=0):
        super().__init__(n)
        self.__Longueur = L
        self.__Largeur = l

    def Surface(self):
        return self.__Longueur * self.__Largeur

    def Perimetre(self):
        return 2 * (self.__Largeur + self.__Longueur)


class Cercle(Forme):
    def __init__(self, n="nom", R=0):
        super().__init__(n)
        self.__Rayon = R

    @property
    def rayon(self):
        return self.__Rayon
        self.__Rayon = R

    @rayon.setter
    def rayon(self, r):
        self.__Rayon = r

    def Surface(self):
        return math.pi+math.pow(self.__Rayon, 2)

    def Perimetre(self):
        return 2*math.pi*self.__Rayon

from abc import ABC, abstractmethod


class Comparable(ABC):
    """
interface permettant de comparer les objets des classes
    """
    @abstractmethod
    def CompareTo(self):
        pass


class AppElectrique(Comparable):
    """
classe appareil Electrique
    """

    def __init__(self, reference=0, puissance=0, poid=0, prix=0):
        self.__reference = reference
        self.__puissance = puissance
        self.__poid = poid
        self.__prix = prix

    @property
    def reference(self):
        return self.__reference

    @reference.setter
    def reference(self, r):
        self.__reference = r

    @property
    def puissance(self):
        return self.__puissance

    @puissance.setter
    def puissance(self, p):
        self.__puissance = p

    @property
    def poid(self):
        return self.__poid

    @poid.setter
    def poid(self, po):
        self.__poid = po

    @property
    def prix(self):
        return self.__prix

    @prix.setter
    def prix(self, pr):
        self.__prix = pr

    def __str__(self):
        return f"reference: {self.reference}, puissance: {self.puissance}, poid: {self.poid}, prix: {self.prix}"

    def CompareTo(self, o):
        # return self.puissance == o.puissance
        if self.puissance == o.puissance:
            return True
        else:
            return False


class energitique:
    def ClasseEneergetique(self):
        if AppElectrique.puissance < 300:
            return f"Class A"
        elif AppElectrique.puissance >= 300 and AppElectrique.puissance < 1000:
            return f"Class B"
        else:
            return f"Class C"


class Television(AppElectrique):
    def __init__(self, reference=0, puissance=0, poid=0, prix=0, typeE="LED", frequence=0):
        super().__init__(reference, puissance, poid, prix)
        self.__typeE = typeE
        self.__frequence = frequence

    @property
    def typeE(self):
        return self.__typeE

    @typeE.setter
    def typeE(self, tE):
        self.__typeE = tE

    @property
    def frequence(self):
        return self.__frequence

    @frequence.setter
    def frequence(self, frequence):
        self.__frequence = frequence

    def __str__(self):
        return f"{super().__str__()}, typeE: {self.typeE},frequence: {self.frequence}"

    def CompareTo(self, o):
        if super().CompareTo(o) and self.frequence == o.frequence:
            return True
        else:
            return False


class VeloElec(AppElectrique):
    def __init__(self, reference=0, puissance=0, poid=0, prix=0, autonomie=0, kilometrage=0):
        super().__init__(reference, puissance, poid, prix)
        self.__autonomie = autonomie
        self.__kilometrage = kilometrage

    @property
    def autonomie(self):
        return self.__autonomie

    @autonomie.setter
    def autonomie(self, tE):
        self.__autonomie = tE

    @property
    def kilometrage(self):
        return self.__kilometrage

    @kilometrage.setter
    def kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    def Rouler(self, d):
        return self.kilometrage + d

    def Charger(self, min):
        return (min * 10) / 60

    def __str__(self):
        return f"{super().__str__()}, autonomie: {self.autonomie}, kilometrage: {self.kilometrage}"

    def CompareTo(self, v):
        return super().CompareTo(v) and self.autonomie == v.autonomie

    def __add__(self, v):
        velo = VeloElec()
        velo.autonomie = self.autonomie + v.autonomie
        velo.kilometrage = self.kilometrage + v.kilometrage
        return velo


v = VeloElec("carbon", 5, 3, 5, 3, 5)
v2 = VeloElec("carbon", 5, 5, 3, 7, 9)
t = Television("LG", 5, 3, 5, "LED", 6)
t2 = Television("LG", 5, 3, 5, "LCD", 3)
print("le velo a avance: ", v.Rouler(55))
print("le velo peut reseter sans charge:", v.Rouler(44))
print(t)
print(v)
print(v.CompareTo(v2))
print(t.CompareTo(t2))

v3 = v + v2
print("new: ", v3)

a = AppElectrique()
print(a.__doc__)
print(Comparable.__doc__)
print(v.__dict__)

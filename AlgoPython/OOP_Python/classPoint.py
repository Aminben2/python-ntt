class Point:
    def __init__(self, x=5, y=5):
        self.__x = x
        self.__y = y

    @property
    def X(self):
        return self.__x

    @X.setter
    def X(self, x):
        self.__x = x

    @property
    def Y(self):
        return self.__y

    @Y.setter
    def Y(self, y):
        self.__y = y

    def __str__(self):
        return f"X = {self.__x}, Y = {self.__y}"

    def __add__(self, P):
        P1 = Point()
        P1.X = P.X + self.X
        P1.Y = P.Y + self.Y
        return P1


P1 = Point(5, 3)
P2 = Point(2, 4)
P3 = P1+P2
print(P3)

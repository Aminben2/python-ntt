class Point:
    # Constructeur:
    def __init__(self, xx=0, yy=0):
        self.x = xx
        self.y = yy

    # Les methods:
    def deplacer(self, dx, dy):
        self.x += dx
        self.y += dy

    def afficher(self):
        print(f"Les courdonnees du point sont: X = {self.x}, Y = {self.y}")

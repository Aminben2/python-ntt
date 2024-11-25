# EXERCICE 2 :
'''def max(a,b) :
    if b<=a :
        return a
    elif a==b :
        return "Les deux nmbres sont égaux"
    else :
        return b
print("le max est", max(float(input("Entrez a")),(float(input("Entrez b ")))))

#EXERCICE 3 :
def paire(a) :
        return a%2==0
if paire(int(input("Entrez un nombre :"))):
    print("Le nombre est paire")
else :
    print("Le nombre n'est pas paire")

#EXERCICE 4 :
def nb_premier(a) :
    i=2
    if i<a and a%i!=0 :
        p=True
    else :
        p=False
    return p
nb = int(input("Entrez un nombre :"))
print(nb_premier(nb))'''

#EXERCICE 6
def moyenne(a,b,c):
    m=(a+b+c)/3
    return m
x = float(input("Entrez le premier nombre :"))
y = float(input("Entrez le deuxième nombre :"))
z = float(input("Entrez le troisième nombre :"))
print(moyenne(x,y,z))

#EXERCICE 7 :
def NCHIFFRES(a) :
    return len(str(a)) #len (chaine) prent en parametre une chaine et
#retourne la longueur de la chaine
print(NCHIFFRES(int(input("Entrez un nombre :"))))

#EXERCICE 8 :
def calcul(nb1,nb2):
    if op=="+" :
        a=nb1+nb2
        return a
    elif op=="-" :
        s=nb1-nb2
        return s
    elif op=="*" :
        m=nb1*nb2
        return m
    else :
        if nb2==0 :
            return "la division impossible"
        else :
            d=nb1/nb2
            return d
a = int(input("Entrez un nombre :"))
b = int(input("Entrez un nombre :"))
op = input("Entrez un opération :")
print(calcul(a,b))





























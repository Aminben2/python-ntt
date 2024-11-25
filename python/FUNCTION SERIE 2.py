#série 2
#EXERCICE 1 : pyramide
"""nb = int(input("Entrez l'hauteur de pyramide :"))
def gen_pyramide(a):
    resultat = ""
    for i in range(a, 0, -1):
        for j in range(i):
            resultat +=" "
        for k in range(a-i+1):
            resultat += "a "
        resultat += "\n"
    return resultat
#POUR L'AFFICHAGE      
print(gen_pyramide(nb))

#EXERCICE 2 :
j = int(input("Entrez le jour :"))
m = int(input("Entrez le mois :"))
a = int(input("Entrez l'année :"))
def correct_date(j,m,a):
    if j<1 or j>31 or m<1 or m>12 or a<1 or (j>28 and m==2) or(j>30 and (m==4 or m==6 or m==9 or m==11)):
        return "Date invalide"
    else :
        return "Date valide"
print(correct_date(j,m,a))"""

#EXERCICE 3 :
nb = int(input("Entrez un nombre :"))
def chiffre_porte_bonheur(nb):
        somme_nb=0
        c=""
        nb = str(nb)
        for i in nb :
            i= int(i)
            somme_nb+=i**2
            print(f"{i}^2 = {int(i)**2}")
            c+=str(int(i)**2)+"+"
        print(f"Nouveau : {c} = {somme_nb}")
        return somme_nb

N= chiffre_porte_bonheur(nb)
while N>=10 :
    N=chiffre_porte_bonheur(N)
if N==1:
    print(f"{nb} est un chiffre porte bonheur")
else :
    print(f"{nb} n'est un chiffre porte bonheur")
    
#METHODE EXE 1 :
"""def gen_pyramide(l):
    for i in range(l):
        for j in range (l-i-1):
            print(" ",end=" ")
        for j in range(i+1):
            print("*",end=" ")
        for j in range(1,i+1):
            print("*",end=" ")
        print()
gen_pyramide(int(input("Entrez l'hauteur de pyramide :")))"""
































    
        
            
    
    

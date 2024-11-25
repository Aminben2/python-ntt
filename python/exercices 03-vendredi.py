#EXERCICE 1: nombre est premier
'''nb=int(input("Entrez un nombre entier positif :"))
while nb <= 0:
    nb=int(input("Entrez un nombre entier positif :"))
i=2
while i< nb and nb % i != 0:
    i+=1
    if i==nb:
        print(f"Le nombre {nb} est premier")
    else:
        print(f"Le nombre {nb} n'est pas premier")

#METHODE 2 EXE 1 :
nb=int(input("Entrez un nombre :"))
while nb<0 :
    nb=int(input("Entrez un nombre :"))
if nb==0 or nb==1:
    print(nb,"est premier")
elif nb==2:
    print(nb,"est non premier")
else :
    nbdiv=0
    for i in range(2,nb):
        if nb%i==0 :
            nbdiv+=1
    if nbdiv==0:
        print(nb,"est premier")
    else:
        print(nb,"est non premier")
# AFFICHAGE 100 NOMBRES PREMIERS :
nb=2
nbp=1
print(nbp,"-",nb)
nb+=1
nbp+=1
while nbp<=100:
    nbdiv=0
    for i in range(2,nb):
        if nb%i==0:
            nbdiv+=1
    if nbdiv==0:
        print(nb)
        nbp+=1
    nb+=1'''

#EXERCICE 2:
'''n = int(input("Entrez un nombre :"))
while n<0 :
    n = int(input("Entrez un nombre :"))
if n==0 or n==1:
    print(nb,"n'est pas parfait")
else :
    s=0
    for i in range(1,n):
        if n%i==0 :
            s+=i
    if n==s :
        print("Le nombre est parfait")
    else:
        print("Le nombres n'est pas parfait")

#EXERCICE 3:
nb=int(input("Entrez un nombre :"))
while nb<=0:
        nb=int(input("Entrez un nombre supérieure à 0 :"))
for i in range(16):
    if nb%2==0 :
        nb = nb // 2
        print(f"u{i} = {nb}")
    else :
        nb = (nb*3)+1
        print(f"u{i} = {nb}")
# METHODE 2
nb=int(input("Entrez un nombre :"))
i=0
while nb!=1:
    if nb%2==0:
        nb=nb//2
        print(f"U{i} =  {nb}")
    else :
        nb=nb*3+1
        print(f"U{i} = {nb}")
    i+=1
if nb==1 and i==0:
    print("U0 =1 ")'''

#EXERCICE 5:
print("X*Y\tI",end="\t")
for i in range(0,11):
    print(i,end="\t")
print()
print("-"*100)
for i in range(0,11):
    print(i,end="\tI\t")
    for j in range(0,11):
        print(f"{i*j}",end="\t")
    print()
#EXERCICE 6:
choix=15
a=None
b=None
while choix!=3:
    choix=int(input('''--------------Menu----
1. Entrez a et b
2. Afficher produit des nombres entre a et b
3. Quitter
Tapez votre choix :'''))
    if choix==1 :
        a=int(input("Entrez a :"))
        b=int(input("Entrez b :"))
        while b<=a :
            b=int(input("Entrez b :"))
    elif choix==2 :
        if a== None and b== None :
            ("il faut entrer a et b choisissez le choix 1")
        else:
            p=1
            for i in range(a+1,b):
                p*=i
            print("Le produit est :", p)
        elif choix==3:
            print("MERCI")
        else:
            print("choix invalide")
    

    


    
      














                  

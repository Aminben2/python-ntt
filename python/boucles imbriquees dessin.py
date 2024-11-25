#BOUCLES IMBRIQUEES / DESSIN:
#Longuer : nombres des lignes
#Largeur : nombres des colonnes
#EXEMPLES :
l = int(input("Entrez la longueur"))
c = int(input("Entrez la largeur"))
for i in range(l) : #lignes //5
    for j in range(c) : #colonnes//5
        print("*",end="")
    print()
#############################"
l = int(input("Entrez la longueur"))
c = int(input("Entrez la largeur"))
for i in range(l) : #lignes
    print("*"*c)
#CARRE VIDE:
l = int(input("Entrez la longueur"))
c = int(input("Entrez la largeur"))
for i in range(l) :
    if i==0 or i==l-1 :
        for j in range(c) :
            print("*",end=" ")
    else :
        for j in range(c):
            if j==0 or j==c-1 :
                print("*",end=" ")
            else :
                print(end="  ")
    print() #pour saut de la ligne
# LES TRIANGLES :
#hauteur : les lignes = Dans un dessin ce qui ce passe dans chaque ligne varie soit augmente ou diminue (la valeur final du fonction range du 2ème boucle est toujours en fonction (i=le compteur de la 1ère boucle)
#augmanté : range de (i)ou(i+1)
#diminue : range(h-i) ou range(h-i-1)
h=int(input("Entrez l'hauteur de triangle"))
for i in range(h):
    for j in range(i+1):
        print("*",end="")
    print()
#triangle inverse:
h=int(input("Entrez l'hauteur de triangle"))
for i in range(h):
    #boucle pour dessiner les espaces(aumenté)
    for j in range(i):
        print(" ",end="")
    #boucle pour dessiner les triangles(diminué)
    for j in range(h-i):
        print("*",end="")
    print()
    ############################################
l=int(input("Entrez la longueur :"))
c=int(input("Entrez la largeur :"))
for i in range(l):
    for j in range(c):
        print("-",end="")
    print()
    ###########################################
l=int(input("Entrez la longueur :"))
c=int(input("Entrez la largeur :"))
for i in range(l):
    if i==0 or i==l-1:
        for j in range(c):
            print("*",end=" ")
    else:
        for j in range(c):
            if j==0 or j==c-1:
                print("*",end=" ")
            else:
                print(end="  ")
    print()




        
    























    


    

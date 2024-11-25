########################################## LES LISTES #####################################
#déclaration des listes :
#type de liste = hétirogène
l = ["we",544645,6.2,True,[4,5,8,7]]
#l = [] #liste vide
#l = list((34."fd",5))
print(l)
#Les listes sont modifiables
#Les listes peut contenir des éléments de type différent
#la fonction len(liste) = retourne le nombre des éléments de la liste
print(len(l))
#indexation : le fait d'accéder à un élément en utilisant des indices
print(l[-1])
#modifier un élément
l[-4] ="xxx"
print(l)
#slicing / tranchage :
print(l[-2:4])
#parcourir une liste :
for i in l :
    print(l)
for i in range(len(l)):
    print(l[i])
#suppression par indice:
#le mot clé del list[ind]= supprime de la liste l'élément qui a l'indice ind
del l[2]
print(l)
#Ajout a la liste :
#methode liste.append(valeur) = ajoute a la fin de la liste la valeur en paramètre
li = [656,'gdh',88.02,"hj",True]
li.append(int(input("Entrez unz nouvelle valeur :")))
print(li)
#methode liste.insert(indice,valeur) = insere  à la position passee en paramètre la valeur passee en parametre
li.insert(2,"r")
print(li)
#On peut ajouter un nouveau element en utilisant la concatenation:
li=li+['hjj',656,8.2]
print(li)
#methode list.extend(liste)
li.extend([1,1,1,5])
print(li)

#exercice moyenne stagiaire : remplissage de la liste par l'utilisateur
nb = int(input("Entrez le nombre des stagiaires :"))
lis =[]
#calcul moyenne
som=0
for i in range(nb) :
    note = float(input("Entrez les notes des stagiaires :"))
    lis.append(note)
    som+=note
print("La moyenne de la classe est :", som/nb)
print("Liste des notes :", lis)
'''liste = lis.copy()
for i in liste :
    if i<10 :
        lis.remove(i)'''
while i<len(lis):
    if lis[i] == 23:
        del lis[i]
    else :
        i+=1
#list.count(valeur) :entier => retourne le nombre d'occurence de la valeur passee en paramètre
#Des méthodes pour la suppression des éléments sur les listes:
"""lis.count(10)
for i in range(lis.count(10)) :
    lis.remove(23)"""
"""cp=0
for i in lis :
    if i<10 :
        cp+=1
for i in range(cp) :
    for j in lis :
        if j<10 :
            lis.remove(j)
        continue"""
print("Liste après suppression des notes inférieures à 10 :", lis)
        
    
#suppression:
#methode list.remove(valeur) = supprime l'element par sa valeur
l3 =[55,34,33.2]
l3.remove(34)
print(l3)
#methode list.pop(indice) = supprime lélément par son indice passee en paramètre
l3.pop(1)
print(l3)
#methode list.clear() = vider la liste
l3.clear()
print(l3)

#methode list.index(valeur, start=0, fin=len(list)-1):entier => retourne l'indice de la première d'occurrence
#de la valeur passee en parametre s'il esxiste sinon (value error)

#method list.sort(reverse=False) ترتب الارقام => trie la liste par ordre croissant si reverse et 
#False et par decroissant si reverse est True

#methode list.reverse() => inverse la liste sans trie

#methode list.copy():liste => retourne une liste copie de la liste appellante
L4=lis.copy() # une copie des valeurs
L5= lis[:] # une copie des valeurs
L6 = lis # une copie d'adresse (création d'une variable qui pointe sur la meme adresse)




























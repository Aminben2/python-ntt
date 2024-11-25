#################################################Les tuples##################################################################"
#Les tuples se sont des collections inmodifiables; on peut ni ajouter ni étendre la tuple ni modifier un de ses éléments
#déclaration de la tuple :
"""t = () #tuple vide
t=(656,25,165,8)
t=("jkknn",56,65.65,True,[56,54])
t= 56,6,32 #sans les parenthèse
t=(4,) #tuple avec un seul élément
t=4,
print(type(t))
# la fonction tuple (iterable=()) = cree ou convertit l'iterable passe en parametre a une tuple
# del supprime tout le tuple
#concatenation: nouveautuple=tuple1+tuple2
t2=t+(45,455,787)
print(t2)
print(list(t2)) #on a convertit la tuple a une list

#Exercice :
tup=(32,265,65,46,2,3,1,89,1,65)
liste=list(tup)
print(liste)
liste.reverse()
ind=liste.index(min(liste))
liste[-1],liste[ind]=liste[ind],liste[-1]
liste.reverse()
tup=tuple(liste)
print(tup)
######################################################DICTIONNAIRES######################################################"
"dictionnaire : c'est une collection qui range les elements sous forme des paires <key:value> ;"
#les cles peuvent etre de n'importe quel type sauf les listes et les dictionnaires tandis que les valeurs peuvent
#le dictionnaire à sens unique
# cle : valeur
#valeur = cle xx(NOO)
# etre de n'importe quel type.
#syntaxe generale d={key1:value1 , key2:value2...}
#la declaration d'un dictionnaire:
d={} #dict vide
d={"hjhk":45, 34:"ghg", True:56.3, (5,4):["jhj",4454]}
print(d)
#niveau 0: <stagiaire : moyenne>
d={"Ahmadi":14, "Karimi":13, "Fatimi":0, "Omari":20}
#niveau 1 : <stagiaire : [note1,note2,note3]> => valeur liste
#niveau 1 : <stagiaire : (note1,note2,note3)> => valeur tuple
d={"ahmadi":[12,6,17], "omari":[12,3,17]}
#niveau 2 : <stagiaire : {mod1:note, mod2:note, mod3:note}>
d={"ahmadi":{"M01":20, "M02":12,"M03":15}, "omari":{"M01":15, "M02":17,"M03":15}}
#parcours par cle
for i in d:
    print(i,d[i]) #i prend la clé et d[i] prend la valeur
#la methode dict.keys() = retourne une liste des cles
    print(d.keys())
for i in d.keys():
    print(i)
    print(d[i])
#methode dict.values() = retourne une liste des valeurs
# Pour connaisser le cle par la valeur:
print(d.values())
for i in d.values():
    print(i) # i prend les valeurs
    for j in d :
        if i == d[j] :
            print(j)
# methode dict.items() = retourne une liste des tuples, chaque tuple regroupe la cle et la valeur
print(d.items())
for i in d.items():
    print(i) # (k1,v1)
    print(i[0]) # la cle
    print(i[1]) # la valeur
for i,j in d.items():
    print(i) # affiche la cle
    print(j) #affiche la valeur

#la modification d'un elements du dict : dict[cle] = nv_valeur

d1={"Ahmadi":14, "Karimi":13, "Fatimi":0, "Omari":20}
d1["Ahmadi"]=20
print(d1)
# Ajouter a la fin du dict : dict[nv_cle]=valeur
d1["Hamidi"]=15
print(d1)
#methode dict.update(dictionnaire): Ajoute le dictionnaire en parametre a la fin du dict(dictionnaire qui appelle)
d1.update({"Tahiri":10, "Rachidi":17}) #ajouer plusieurs elements a la dict
print("apres l'ajout", d1)
#remplissage d'un  dictonnaire : NV 0 => {Nstagiaire : moyenne}
stagiaire = {}
nb=int(input("Entrez le nombre d'éléments :"))
for i in range(nb):
    S=input("Entrez le nom du stagiaire :")
    moy=float(input("Entrez la moyenne :"))
    stagiaire.update({S : moy})
print("Le dictionnaire est :", stagiaire)

#remplissage d'un  dictonnaire : NV 1 => {Nstagiaire : [n1,n2,nn..]}
stagiaire = {}
nb = int(input("Entrez le nombre d'éléments :"))
n = int(input("Entrez le nombre des modules :"))
for i in range(nb):
    S = input("Entrez le nom du stagiaire :")
    moyennes = []  

    for j in range(n):
        moy = float(input("Entrez la note de module :"))
        moyennes.append(moy)  

    stagiaire.update({S : moy})  

print("Le dictionnaire est :", stagiaire)

stagiaire = {}
nb = int(input("Entrez le nombre des stagiaires :"))
Nmod = int(input("Entrez le nombre des modules :"))

for i in range(Nmod):
    mod = input("Entrez le nom du module :")
    dic = {}  
    for j in range(nb):
        S = input("Entrez le nom du stagiaire :")
        note = float(input("Entrez la note du module :"))
        dic.update({S: note})  

    stagiaire.update({mod: dic})  

print("Le dictionnaire est :", stagiaire)

#La suppression d'un seul élément par cle:
#mot cle del : del dict[cle]
#methode dict.pop(cle)

stg={"Ahmadi":20, "Karimi":15, "Omari":7, "Farissi":12, "hamidi":9}
stgc=stg.copy()
for i in stgc.values():
    if i<10:
        for j in stgc :
            if i == stgc[j] :
                stg.pop(j)
print(stg)

#methode dict.popitem() =>  supprime le dernier element
#methode dict.clear() => vide le dictionnaire
#methode dict.fromkeys(listcle,valeur=None):dictionnaire => cree et retourne un dict dont chaque cle est un element de la liste
#^passe en parametres et la valeur de chaque cle et la valeur ^passee en parametre
d={}
l=["p1","p2","p3"]
print(d.fromkeys(l,12))

#methode dict.get(cle,defaultvalue=None) => retourne la valeur de la clee passee en parametre
print(stg.get("ch",0))
print(stg.setdefault("Karimi",0))

#Exercice 1:

def dictionnaire(ch):
    dic = {}
    for i in ch:
        c = 0
        for j in ch:
            if i == j:
                c += 1
        dic.update({i: c})

    return dic

ch = input("Entrez une chaine :")

print(dictionnaire(ch))
#methode count:
def dictionnaire(ch):
    dic = {}
    for i in ch:
        dic[i]=ch.count(i)
    return dic

ch = input("Entrez une chaine :")

print(dictionnaire(ch))
"""
#Exercice 2:
'''def dictionnaire_etudiants(chaine):
    dict_etudiants = {}
    l= chaine.split('\n')
    for i in l:
            element = i.split(';')
            cin = int(element[0])
            nom_prenom = ' '.join(element[1:])
            dict_etudiants[cin] = nom_prenom
    return dict_etudiants

chaine_etudiants = """213615200;BESNIER;JEAN
213265646;DUPOND;MARC
212656568;DURAND;JULIE"""

Dict_etudiants =dictionnaire_etudiants(chaine_etudiants)
print(Dict_etudiants)'''

#Exercice 3:
#b
def Nb_Tventes(dictionnaire):
    s=0
    for i in dictionnaire.values():
        s+=i
    return s
#c
def nom_vendeur(dictionnaire):
    m=max(dictionnaire.values())
    for i in dictionnaire:
        if dictionnaire[i]==m:
            return i
            
#d
def Supprime_bas_vendeur(dictionnaire):
    mini=min(dictionnaire.values())
    l=[]
    for i in dictionnaire:
        if dictionnaire[i]==min :
            l.append(i)
    for i in l:
        dictionnaire.pop(i)
#e
def Supprimer(dictionnaire,nomv):
    d.pop(nomv)

#g
def Modifier(d,nomv):
    #dic[cle]=nv_valeur
    d[nomv]=int(input("Entrez lz nouveau nombre des ventes :"))

#f
def Dict_Trie(dictionnaire):
    d_trie={}
    for i in sorted(dictionnaire.values(), reverse=True):
        for j in dicrionnaire:
            if dictionnaire[j]==i :
                d_trie[j]=i
    return d_trie

#Pour trier le dictionnaire par rapport a ses valeurs et retourne une liste des cles
print(sorted(d,key=d.get))

#h
def enregistrer_ventes(d):
    f=open("filex.txt", "w")
    for i,j in d.items():
        ligne=f"{i} => {j}\n"
        f.write(ligne)
    f.close()
        
        

#Programme Principal : Menu
while True :
    choix=int(input("""-------------Menu-------------
1 : Ajouter les ventes
2 : Afficher les ventes.
3 : Afficher les ventes triées.
4 : Modifier les ventes d’un vendeur .
5 : Rechercher les ventes d’un vendeur .
6 : Supprimer un vendeur .
7 :Afficher le nombre total des ventes
8 :Afficher le vendeur qui a réalisé plus de vente
9 : Enregistrer dans un fichier
10: Quittez le programme
Tapez votre choix :"""))
    if choix==1 :
        nb=int(input("Entrez le nombre des vendeurs :"))
        dic={}
        for i in range(nb):
            Nvendeur=input("Entrez le nom du vendeur :")
            Nventes=int(input("Entrez son nombre de ventes :"))
            dic.update({Nvendeur: Nventes})
    elif choix==2:
        for i,j dic.items():
            print(f"Nvendeur: {i} = Nbre ventes : {j}")
    elif choix==3:
        for i,j in Dict_Trie(Nventes).items():
            print(f"Vendeur : {i} = Nbre ventes : {j}")
    elif choix==4:
        nomv=input("Entrez le nom du vendeur :")
        print(Modifier(dic,nomv))  
    elif choix==5:
        nom_vendeur_recherche = input("Entrez le nom du vendeur à rechercher : ")
        print(f"Les ventes de {nom_vendeur_recherche} sont : {ventes.get(nom_vendeur_recherche, 'Vendeur non trouvé')}")
    elif choix==6:
        nvendeur_supp=input("Entrez le nom du vendeur qui va supprimer :")
        print(Supprimer(dic,nvendeur_supp))
    elif choix==7:
        print(Nb_Tventes(dic))
    elif choix==8:
        print(nom_vendeur(dic))
    elif choix==9:
        pass
    elif choix ==10:
        print("Programme terminé.")
        break
    else :
        print("Choix invalide.")
    
    
"""for i in d.values():
    print(i) # i prend les valeurs
    for j in d :
        if i == d[j] :
            print(j)"""


























    
    
    

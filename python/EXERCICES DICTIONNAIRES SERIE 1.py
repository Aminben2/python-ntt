#Exercice 4:
def remplir(d):#d il existe dans p.principale
    nb=int(input("entrez le nombre des stagiare :"))
     nbm=int(input("entrez le nombres des module:"))
     liste=[]
    for i in range(nbm):
         liste.append(input("entrez le nome de modues:"))
    for i in range(nb):
        nom=input("entrez le nom de stagiare :")
        mod={}
        for j in liste:
            note=float(input("entrz le notes :"))
            mod[j]=note
        d[nom]=mod
        
def moyenne(d):
    for i,j in d:
       m= sum(j.values())/len(j)
       print(f"la moyenne du stagiare {i} est {m}")

       
def supprimer(d,nom):
    if nom in d:
        d.pop(nom)
    else:
        print("ce stagiaire n'est existe pas")

def moyenne(d):
    s=0
    for i,j in d:
       m= sum(j.values())/len(j)              # la moyenne de chaque stqgiaire 
       s+=m
    return s/len(d)
def trier(d):
    d_t={}
    for i in sorted(d.keys()):
        d_t[i]=d[i]
    return d_t
def modifier(d,nom):
    if nom in d:
       mod={}
       for i in range(3):
            nom_mod=input("entrez le nom de la module :")
            note=float(input("entrz le notes :"))
            mod[nom_mod]=note
        d[nom]=mod
    else:
        print("le stagiare n'est exsite pas")

            
#Exercice 5:
Produits = {"p1_563": ["lait",12.3,14,63], "p2_897": ["yaourt",2.3,3,200], "p1_563":
["jus",5,6.3,80]}
#q1:
##1
def remplir(d):
    nb=int(input("entrez le nmbre des elements du dictionnaire:" ))
    for i in range(nb):
        code=input("entrez la reference du produit:")
        nom=input("entrez le nom du produit:")
        pa=float(input("entrez le prix d'achats:"))
        pv=float(input("entrez le prix de vente:"))
        qte=int(input("entrez la quantite en stock:")) 
        d.update({code:[nom,pa,pv,qte]})
"""d[cod]=[nom,pa,pv,qte]"""
        
    
##2
def rechercher(d,cp):
    return cp in d

##3
def modifier(d,cp):
    if cp in d:
        nom=input("entrez le nv nom du produit:")
        pa=float(input("entrez le nv prix d'achats:"))
        pv=float(input("entrez le nv prix de vente:"))
        qte=int(input("entrez la nv quantite en stock:")) 
        d[cp]=[nom,pa,pv,qte]
    else:
        print("ce produit n'existe pas")
        
##4
def supprimer_produits(d):
    dc=d.copy()RR
    for i,j in dc.items():
        if j[-1]==0:
            d.pop(i)
            
##5
def nbreprdstock(d):
    s=0
    for i in d.values():
        s+=i[-1]
    return s
####
##6-a
def remplirdclt(d , dp):
    nbclt=int(input("entrez le nombre des clients:"))
    for i in range(nbclt):
        cc=input("entrez le code du client:")
        nba=int(input("entrez le nombre des produits achetes:"))
        prd={}
        for j in range(nba):
            ref=input("entrez la reference du produit achetez:")
            if ref in dp
                qte=int(input("entrez la quantite achetes:"))
                prd[ref]=qte
            else:
                print("ce produit n'execite pas")
        d[cc]=prd
        
##6-b
def prix_a_payer(dp,dc):
    for i,j in dc.items(): #i: cle / j :valeur(dictionnaire)
        p=0
        for k,l in j.items(): # k: cle (reference de produits) / l:valeur ( qte achete du prd)
            p+=dp[k][2]*l
        print(f"le client {i} a paye :{p} dh ") 
dp={"p1":["lait",11,22,44],"p2":["lait",15,22,77],"p3":["lait",141,232,44]}
dc={"clt1":{"p1":5,"p2":2},"clt2":{"p1":8,"p2":44},"clt3":{"p1":22,"p2":135}}


###6-c
def prix_totale(dp,dc):
    p=0
    for i,j in dc.items(): #i: cle / j :valeur(dictionnaire)
        for k,l in j.items(): # k: cle (reference de produits) / l:valeur ( qte achete du prd)
            p+=dp[k][2]*l
    return p

###7
def stocker(d):
    f=open("filecc.txt", "w+")
    for i,j in d.items():
        ligne = f"{i} => {j}\n"
        f.write(ligne)
    f.close()
    f=open("filecc.txt", "r+")
    result=f.read()
    f.close()
    return result

############# programme principale ###############
while True :
     prd={}
     remplir(prd)
     choix=int(input("""------------------menu--------------------
    1- rechercher un produit
    2- modifier un produit
    3-supprimer le produit qui n'existe pas dans le stock
    4-afficher la quantiter total
    5- afficher les information de chaque produit
    6-enregistrer dans un fichier
    7-quitez le programme
    tapez votre choix :
    """))
     if choix==1:
         cd=input("entrez le code de produite que vous voulez rechercher:")
         if rechercher(prd,cd)==True:
             print("ce produit existe")
         else:
             print("ce produit n'est existe pas")
     elif choix==2:
         cd=input("entrez le code de produite que vous voulez modifier:")
         modifier(prd,cd)
     elif choix==3:
         supprimer_produits(prd)
     elif choix==4:
         print("la quqntiter total est est",nbreprdstock(prd))
     elif choix==5:
         for i,j in prd.items():
             print(f"ref:{i} , nom{j [0]}, prix achat :{j[1]},prix vente:")
             print(f"{j[2]}quantitez en stock :{j[-1]}")
     elif choix==7:
         print("fin programme ")
         break
     else:
         print("choix invalide")


























    


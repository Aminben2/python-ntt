#EFM-DEV-V1-2023#:
#Ecercice 1:
def estADN(mot):
    ch="ACGT"
    for i in mot :
        if i not in ch:
            return False
    return True
mot="ACGT"
print("mot",estADN(mot))
m="TTGAC"
print("m",estADN(m))
m1="GCAATAG"
print("m1",estADN(m1))
m2="AMOG"
print("m2",estADN(m2))
m3="CaTg"
print("m3", estADN(m3))
#Exercice 2:
#facto
def facto(nb):
    if nb==0:
        return 1
    return nb*facto(nb-1)
#suite
def suiteUN(nb):
    if nb==0:
        return -1
    elif nb==1:
        return 1
    else:
        return facto(nb)*((1/2*suiteUN(nb-1))+(3/4*suiteUN(nb-2)))
'''#dessin
def Dessiner(nb):
    for i in range(nb):#0
        for j in range(nb,i,-1):
            print(" ",end="")
        print()
    for k in range((i * 2) - 1):  
            if k == 0 or k == (i * 2) - 2:
                print(f"U{i}", end="")
            else:
                print(" ", end="")
    print()



nb=5
facto(nb)
suiteUN(nb)
Dessiner(nb)
'''
#Partie II:
#Exercice1
def Som(ch):
    if ch.startswith("+") or ch.endswith("+"):
        return -1
    sym="/*-]})&'([{|`\^@"
    for i in ch:
        if i.isalpha() or i in sym:
            return -1
    for i in range(len(ch)):
        if (ch[i]=="+") and (ch[i+1]=="+"):
            return -1
    c=ch.split("+")
    som=0
    for i in c:
        som+=int(i)
    return som
t1 = Som("3+8")
print(t1)
print(Som("6+5++9+4"))
#Exercice 2:
'''def facto(p):
    if p==0:
        return 1
    return p*facto(p-1)

def produit(n,k):
    if k==0:
        return 1
    if n>k :
        return n*produit(n+1,k)

def binomial(n, k):
    if n >= k:
        return facto(n) // (facto(k) * facto(n - k))
    else:
        return 0

def liste_binomiaux(n):
    l = [binomial(n, k) for k in range(n + 1)]
    return l

print(facto(3))
print(produit(6,3))
print(liste_binominaux(6))
'''
#Exercice 3: Dictionnaire
#1
d = {}
with open("info.txt", "r+") as f:
    for i in f:
        info = i.strip("\n").split(";")
        Location = info[0]
        Nom = info[1]
        date = info[2]
        immatricule = info[3]
        marque = info[4]
        d[Location] = {"Nom_Client": Nom,
                       "Date": date,
                       "immatricule": immatricule,
                       "marque": marque
                       }
print(d)
print()
#2
def afficher_location(d):
    for i,j in d.items():
        print(f"Location: {Location}")
        for k,l in j.items():
            print(f"{k}: {l}")

    
#3
def modifier_location(d,num):
    if num in d.keys():
        d[num]["Nom_Client"]= input("Entrez le nom du client:")
        d[num]["Date"]=input("Entrez la date de location:")
        d[num]["immatriculation"]=input("Entrez l'immatriculation:")
        d[num]["Marque"]=input("Entrez la marque:")
        print("Le dictionnaire a été modifier avec succès")
    else:
        ("Ce numéro n'existe pas")
''''''

#4
def supprimer_location(d,num):
    if num in d.keys():
        d.pop(num)
        print("La suppresion à effectuée")
    else :
        print("Le numéro n'existe pas")

#5
def meilleur_voiture(d):
    compteur_v={}
    for i,j in d.items():
        compteur_v[immatricule]=compteur_v.get(immatricule,0)+1
    v_max=max(compteur_v, key=compteur_v.get)
    return v_max

#6
while True:
    choix = input("""-----------------------MENU---------------------
1-Afficher Locations
2-Modifier Location
3-Supprimer Location
4-Afficher la voiture la plus louée
5-Quitter
Entrez votre choix : """)

    if choix == "1":
        print("Les informations de chaque location sont :", afficher_location(d))
    elif choix == "2":
        modifier_location(d, input("Entrez un numéro"))
        print("Les informations de la location ont été modifiées avec succès.")
    elif choix == "3":
        supprimer_location(d, input("Entrez un numéro"))
        print("La location a été supprimée avec succès.")
    elif choix == "4":
        print("La voiture la plus louée a l'immatriculation :", meilleur_voiture(d))
    elif choix == "5":
        print("Fin")
        break
    else:
        print("Choix invalide")

    

    






























































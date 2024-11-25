#Exercice 1: Chaine en majuscule
ch = input("Entrez un chaine :")
print(ch.upper())
#En algorithme :
''' Algorithme chaine_majuscule
Variables
ch : chaine
Debut
Exrire("Entrez une chaine :")
Lire(ch)
Ecrire(ch en majuscule)
Fin'''

#Exercice 2: compte le nombre d'occurrence d'une lettre
ch = input("Entrez une chaine :")
lettre = input("Entrez la lettre à rechercher :")
occu = ch.count(lettre)
print(f"Le nombre d'occurences de la lettre {lettre} dans la chaine est {occu}")

#En algorithme
'''Algorithme nbre_occurrence
Variables
ch , l : chaine
i, occ : entier
Debut
Ecrire("Entrez une chaine :")
Lire(ch)
Ecrire("Entrez la lettre à rechercher :")
Lire(l)
occ <- 0
Pour i allant de ch
    Si i = l alors
        occ <- occ+1
    FinSi
FinPour
Ecrire("Le nombre d'occurrences de la lettre", l, "dans la chaine est :", occ)
Fin'''

#Exercice 3: compte le nombre des lettres et nombres
ch = input("Entrez une chaine :")
cl = 0
cn = 0
for i in ch :
    if i.isalpha() :
        cl+=1
    elif i.isdigit() :
        cn+=1
print(f"Le nombre d'occurrences de lettre est {cl} et de chiffre {cn}")

#Exercice 4: le nombre de répétition de chaque caractère
chaine = input("Entrez une chaine :")
c = {}
for i in chaine :
    c[i] = chaine.count(i)
print(f"Le nombre de répétition de chaque caractère de la chaine {chaine} est : {c}")

#En algorithme:
''' Algorithme nombre_répétition
Variables
chaine : chaine
i,j,c : entier
Debut
Ecrire("Entrez une chaine :")
Lire(chaine)
Pour chaque i dans chaine
    c<-0
    Pour chaque j dans chaine
        Si i = j alors
            c<-c+1
        FinSi
    FinPour
    Ecrire("Le nombre de répétition du caractère", i, "est :", c)
FinPour
Fin'''

#exe 4 : methode
c="Hello World"
s=""
for i in c:
    if i not in s:
        print(f"{i} : {c.count(i)} fois")
        s+=i

#Exercice 5: le nombres des voyelles
chn = input("Entrez une chaine :") 
voyelles = "aieouy"
c=0
for i in chn:
    if i.lower() in voyelles:
        c+=1
print(f"Le nombre de voyelles dans la chaine '{chn}' est : {c}")

#En algorithme:
'''Algorithme voyelles
Variables
ch : chaine
c,i : entier
Debut
Ecrire("Entrez une chaine :")
Lire(ch)
c <- 0
Pour chaque i dans ch
    Si i="a" OU i="i" OU i="e" OU i="o" OU i="u" i="A" OU i="I" OU i="E" OU i="O" OU i="U" alors
        c<-c+1
    FinSi
FinPour
Ecrire("Le nombre de voyelles dans la chaine", ch, "est :", c)
fin'''

#Exercice 6: supprime toutes les lettres (e)
ch = input("Entrez une chaine :")
c=''
for i in ch:
    if i!= "e":
        c+=i
print(f"La chaine '{ch}' est changée à {c}")

#exe6 : methode
ch = input("Entrez une chaine :")
print("La chaine sans 'e' est:", c.replace("e",""))

#En algorithme :
'''Algorithme supprime_lettre
Variables
c,ch,lettre : chaine
i : caractère
Debut
Ecrire("Entrez une chaine :")
Lire(ch)
lettre = "e"
c<-""
Pour chaque i dans ch
    Si i<>lettre alors
        c <- c+i
    FinSi
FinPour
Ecrire("La chaine", ch, "est changée à", c)
Fin'''

#Exercice 7: supprime toutes les voyelles
ch = input("Entrez une chaine ne dépasse pas une ligne :")
voyelles = "aieouy"
c=''
for i in ch:
    if i.lower() not in voyelles:
        c+=i
print(f"La nouvelle chaine '{ch}' est changée à {c}")

#En algorithme: 
'''Algorithme voyelles
Variables
ch : chaine
c,i : entier
Debut
Ecrire("Entrez une chaine :")
Lire(ch)
c <- ""
Pour chaque i dans ch
    Si i!="a" OU i!="i" OU i!="e" OU i!="o" OU i!="u" i!="A" OU i!="I" OU i!="E" OU i!="O" OU i!="U" alors
        c<-c+i
    FinSi
FinPour
Ecrire("La chaine", ch, "est changée à", c)
Fin'''

#Exercice 8: supprime les caractères doublons
ch = input("Entrez un texte :")
c = ''

for i in ch:
    if i not in c:
        c += i
print(f"La chaine '{ch}' est changée à {c}")

#En algorithme :
'''Algorithme supprime_doublons
Variables
ch,c : chaine
i: caractère
Debut
Ecrire("Entrez un texte :")
Lire(ch)
c<-""
Pour chaque i dans ch
    p<-0
    Tantque p<LONUEUR(c) ET i<>souschaine(c,p+1,1)
        p<-p+1
    FinTantque
    Si p=0 alors
        c<-c+i
    FinSi
FinPour
Ecrire("La chaine", ch, "est changée à", c)
Fin
'''
print()
print()
#Exercice 9:
liste = ['girafe', 'tigre', 'singe','souris']
voyelles = "aeiouy"
v=0
c=0
for i in liste:
    print(i)
    taille = len(i)
    print(f"La taille du chaine '{i}' est {taille}")
    for j in i :
        if i.isalpha():
            if j.lower() in voyelles
                v+=1
            else :
                c+=1
    print(f"Le nombre de voyelles est {v} et de consonnes {c} dans la chaine {i}")

#En algorithme :
'''Algorithme liste
Variables
liste : tableau
i,v,c : entier
Debut
liste<-['girafe', 'tigre', 'singe','souris']
Pour chaque i dans liste
    taille<-LONGUEUR(i)
    Ecrire("La chaine ", i, " a une taille de ", taille, " caractères")
FinPour
Pour chaque i dans liste
    v<-0
    c<-0
    Pour chaque j dans i
        Si j="a" OU j="i" OU j="e" OU j="o" OU j="u" j="A" OU j="I" OU j="E" OU j="O" OU j="U" alors
            v<-v+1
        Sinon
            c<-c+1
        FinSi
    FinPour
    Ecrire("Le nombres des voyelles", v, "est des consonnes", c, "dans" ,i)
FinPour
Fin'''

        
            



        




































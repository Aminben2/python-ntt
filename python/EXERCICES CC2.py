#exercice4
"""def lisrev(L):#[je suis reche]
    lr=[]
    for i in L:
        lr.append(i[::-1])
    return lr
print(lisrev(["je " , "suis"," reche"]))
#Exercice 2 : anagramme
def Procedure_Anagramme(ch1,ch2):
    if len(ch1) == len(ch2):
        for i in ch1: #aimer
            if i not in ch2:#maire
                r = "n'est pas anagramme"
                break
            else :
                r="anagramme"
            
        print(f"La chaine {ch1} et {r} de la chaine {ch2}")
ch1 =input("Entrez la première chaine :")
ch2 =input("Entrez la deuxième chaine :")
Procedure_Anagramme(ch1, ch2)

#Exercice 3 : Hamming
def funct_Hamming(c1,c2):
    if len(c1)==len(c2) :
        d = 0
        for i in range(len(c1)):
            if c1[i] != c2[i]:
                d+=1
        return d
    else:
        return -1
c1 =input("Entrez la première chaine :")
c2 =input("Entrez la deuxième chaine :")
resultat = funct_Hamming(c1,c2)
if resultat != -1:
    print(f"La distance de Hamming entre {c1} et {c2} est : {resultat}")
else :
    print(f"La distance de Hamming entre {c1} et {c2} est : {resultat}")
    
#cc2 dev101 : suite Fibonacci
def fibonacci(n):
    if n<=1 :
        return n
    else :
        return fibonacci(n-1)+fibonacci(n-2)
n_max = int(input("Entrez un nombre :"))
for i in range(n_max) :
    print(f"Fibonacci({i}) = {fibonacci(i)}")
#En algorithme :
Algorithme Fibonacci
Variables
n : entier
Fonction récursive fibonacci(nb : entier)
    Si nb<=1 alors
        retourne 1
    Sinon
        retourne fibonacci(nb-1) + fibonacci(nb-2)
    FinSi
FinFonction
Debut
Ecrire("Entrez un nombre :")
Lire(n)
Pour i allant de 0 à n
    Ecrire("Fibonacci (", i, ") = ", fibonacci(i))"""

#cc2 dev103: exe1
def function_Un(nb):
    if nb==1 or nb==2 :
        return 1
    return 2*(function_Un(nb-1))- function_Un(nb-2)
print(function_Un(4))
def function_Vn(nb):
    if nb == 0 or nb == 1 :
        return 1
    else :
        return 3*function_Un(nb) + function_Vn(nb-1)
#Programme Principale:
"""
N= int(input("Entrez un nombre :"))
liste=[]
for i in range(1,N+1):
    liste.append(function_Vn(i))
print(f"U{N} = {function_Un(N)}")
print(f"V{N} = {function_Vn(N)}")
print("Liste des termes de la série Vn :", liste)
#Triangle:
langueur = len(liste)
print("Liste saisie :", end="|")
for i in range(langueur):
    print(f"V{i} |", end="")
print()
for i in range(langueur,0,-1):
    result = "*".join([f"V{j}" for j in range(langueur,langueur-i, -1)])
    print(result)

#Exercice 2 Q1 cc101 : Trier
L = ["Je","suis","riche"]
#methode1 : avec la fonction list() : elle convertit un iterable en paramètre a une liste
def listeTrie(L):
    ltrie=[]
    for i in L:
        l=list(i) #convertit la chaine a une liste ["J","e"]
        l.sort(reverse=True)#["e","J"]
        print(l)
        c="".join(l) #"ej"
        ltrie.append(c)
    return ltrie
print(listeTrie(L))
#methode 2 : avec la fonction sorted(iterable : c'est une collection de plusieurs éléments):list = elle trie
#les elements de l'iterable passee en parametres et retourne une liste trie
sorted("HELLO") # ["E","H","L","L","O"]
def listTrie(L) :
    ltrie=[]
    for i in L:
        l=sorted(i, reverse=True) #l=["e","J"]
        c="".join(l)
        ltrie.append(c)
        #ltrie.append("".join(sorted(i))) = 3lignes en une ligne
    return ltrie
print(listTrie(L))
#Q2:
def lTrievc(L):
    ltrie=[]
    voy="aieuoyAIUEYO"
    for i in L:
        v="" #chaine des voyelles
        c="" ##chaine des consonnes
        for j in i:
            if j in voy:
                v+=j
            else :
                c+=j
        ltrie.append("".join(sorted(v)+sorted(c)))
    return ltrie
print(lTrievc(L))

#Exercice : somme des chaines
ch= input("Entrez une chaine des nombres ex:(12+14+17) :")
def chSomme(ch):
    for i in range(len(ch)):
        if (48<=ord(ch[i])<=57 or ord(ch[i])==43) and not (ch.endswith("+") or ch.startswith("+")):
            t=True         
        else :
            return -1
    for j in range(len(ch)):
                if ch[j]=="+" and ch[j+1]=="+" :
                    return -1
    if t==True:
        liste=ch.split("+")
        s=0
        for i in liste:
            s+=int(i)
        return s
print(chSomme(ch))
print(dir(str))

#Exercice 2 : cc2 103
def NbrCarct_Upper(ch):
    nbr=0
    for i in ch : #Bonjour
        if i.isupper() :
            nbr+=1
    return nbr

def NbrChiffre(ch):
    chiffre=0
    for i in ch:
        if i.isdigit():
            chiffre+=1
    return chiffre

#Programme Principale:
chaine=input("Entrez une chaine :")
mot = chaine.split()
for i in mot :
    print(f"Le nombre des majuscules est: {NbrCarct_Upper(i)} et le nombre de chiffre est: {NbrChiffre(i)}")
"""


























    
            
    












    

'''
1 - Le role de la fonction Rang en algorithme :
c'est une fonction rechercher dans la chaine la sous chaine
passe en parametres et retourne sa premiere occurence
s'il exixste sinon retourne -1
2 - le mot clé global dans les fonctions utilisé pour modifier
la valeur globale au sein d'un fonction
3 - la diffférence entre les deux :
LC=L si vous modifier la valeur du L, il modifier LC aussi
mais la variable LC=L.copy() ne change pas modifir juste L
'''
#EX01:
def SupprimeVoy(liste):
    voy="aeiyuoAEIYUO"
    L=[]
    for i in liste:
        ch=""
        for j in i:
            if j not in voy:
                ch+=j
        L.append(ch)
    print("La nouvelle liste sans voyelle:", L)
L=["bonjour","le","monde"]
SupprimeVoy(L)

nbC=int(input("Entrez le nombre de caractere d'une liste :"))
liste=[]
for i in range(nbC):
    caract=input("Entrez un caractère :")
    liste.append(caract)
SupprimeVoy(liste)
#EX02:
def facto(nb):
    if nb==0:
        return 1
    return nb*facto(nb-1)
def suite(nb):
    if nb==0:
        return -1
    elif nb==1:
        return 1
    else :
        return facto(nb)*(3*suite(nb-1)+suite(nb-2))
nb=int(input("Entrez un nombre :"))
print(f"la suite du nombre {nb} est {suite(nb)}")

#Ex03:
def lettreDiff(n1,n2):
    if len(n1)==len(n2):
        for i in range(len(n1)): #chat
            if n1[i]!=n2[i]:
                return True
        return False
    return False
n1=input("Entrez le premier mot :")
n2=input("Entrez le deuxieme mot :")
print(lettreDiff(n1,n2))

#EXEMPLE : différence entre isdigit/isdecimal/isnumeric
'''
isdigit :
"123".isdigit() # True
"12.3".isdigit() # False
"²54".isdigit() # False
isdecimal :
"123".isdecimal() # True
"12.3".isdecimal() # False
"²54".isdecimal() # False
isnumeric:
"123".isnumeric() # True
"12.3".isnumeric() # False
"²54".isnumeric() # True
'''
#################################################
#exercice1
def Fibonacci(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    return Fibonacci(n-1)+Fibonacci(n-2)

##Exercice2
def listeTrie(liste):
    l=[]
    for i in l:
        l.append(i[::-1])
    return l
print(listeTrie(["bonsoir"]))
#P1:inversee
"""
def lisrev(L):#[je suis riche  ]
    lr=[]
    for i in L:
        lr.append(i[::-1])
    return lr
print(lisrev(["je " , "suis"," riche"]))
"""
#pare order  alphabitique
#1premier methode
"""
def  listetrie (L):#[je suis riche  ]
    listrie=[]
    for i in L:
        l=list(i)#on convertire la chaina une liste ["J", "e"]
        l.sort(reverse=True)#["e","J"]
        c="".join(l)#"eJ"
        listrie.append(c)#["eJ"]
    return listrie
print(  listetrie(["Je " , "suis"," riche"]))
"""
#2eme methode

def  listetrie (L):#[je suis riche  ]
    listrie=[]
    for i in L:
        l=sorted(i , reverse=True)#["e","J"]
        c="".join(l)#"eJ"
        listrie.append(c)#["eJ"]
        # listrie.append("".join(sorted(i)))
    return listrie
print(  listetrie(["Je " , "suis","riche"]))

###################################################""
###P2
"""
def ordr_alpha (L):
    NL=[]
    for i in L :#[je suis reche  ]
        d=""
        v=""
        for j in i :
            if j in "aeyuioAEYUIO":
                v+=j
            else:
                 d+=j
        NL.append("".join(sorted(v)+sorted(d)))
    return NL
print(ordr_alpha(["Je" , "suis","riche"]))
"""
###############################################################"
#programme principale
#P3
"""
def  Ascii(L):
    ch=""
    for i in L:
        for j in i :
            ch+=str(ord(j))
    return ch
L = input("entrz un chaine")
ls=L.split()
print(ls)
print(Ascii(ls))
"""


            
    




























    

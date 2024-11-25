#Ex01:
def Fibonacci(nb):
    if nb==0:
        return 1
    else:
        return Fibonacci(nb-1)+Fibonacci(nb-2)
#En algorithme:
'''Fonction Fibonacci(nb)
    Debut
    Si nb=0 alors
        retourne 1
    Sinon
        retourne Fibonacci(nb-1)+Fibonacci(nb-2)
    FinSi
FinFonction
#Ex02
Q1:'''
def listeTrie(liste):
    liste_trie=[]
    for i in liste:
        chaine_trie=''.join(sorted(i, reverse=True))
        liste_trie.append(chaine_trie)
    return liste_trie
liste=["Bonsoir","je","suis","malade"]
print("la liste trie est :", listeTrie(liste))
#Q2:
def Trie_ordre_alpha(liste):
    voy="aeiuoyAEIUOY"
    listeT=[]
    for i in liste:
        if i[0] in voy:
            chaineT=''.join(sorted(i, reverse=True))
            listeT.append(chaineT)
        else :
            chaineT=''.join(sorted(i, reverse=True))
            listeT.append(chaineT)
    return listeT
liste=["Bonsoir","je","suis","malade","et","pauvre"]
print("la liste trie est :", Trie_ordre_alpha(liste))          
            


























            

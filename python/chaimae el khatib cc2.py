'''
-La différence entre la fonction et la procédure : les fonctions retourne la résultat
et les procédures ne retourne rien faire juste l'affichage de la résultat.
-La différence entre les méthodes isalpha() et isalnum(): isalpha() proposer la question est ce que
la chaine est contient les alphabet et retourne True sinon retourne False. Et isalnum() retourne True si la chaine
contient juste les chiffres et les alphabet sinon retourne False.
-La différence entre l'appel par mot-clé ou par position : exemple :
l'appel par mot_clé : [Nom,CIN,Prenom]
l'appel par position : ["Ahmedi","Ahmed","L655345"]
'''
#Exercice 2:
#1
def facto(p):
    if p==0 :
        return 1
    return p*facto(p-1)
#2
def produit(n,k):
    if n==0 or k==0 :
        return 1
    elif n>=k :
        for i in range(1,k+1):
            resultat=n*(n-i)*(n-(k-i))
        return resultat
#3
def binomial(n,k):
    if n==0 or k==0 :
        return 1
    elif n>=k :
        return (binomial(n,k))/(facto(k))
#4
def liste_binomiaux(n):
    liste=[]
    for i in renge(1,n+1):
        liste.append(binomial(i))
    return liste
#Exercice 1:
def dessin(ch):
    for i in range(len(ch)+1):
        for j in range(i-1,len(ch)):
            print(ch[j],end="")
        print()
    for i in range(1,len(ch)+1):
        for j in range(i):
            print(ch[j],end="")
        print()
dessin("Programmation")
#Exercice 3:
def BubbleSort(liste):
    for i in range(len(liste)):
        for j in range(len(liste)-i-1):
            c=liste[j]
            if liste[j]>liste[j+1]:
                liste[j+1]=c
    return liste
liste=[34,12,22,11,64,90]
BubbleSort(liste)



































            


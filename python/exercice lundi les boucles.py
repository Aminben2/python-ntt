#EXERCICE 5
'''print("EXERCICE 5")
nb1 = float(input("Entrez un nombre :"))
maxi = nb1
c = 1
while nb1!=0 :
    c+=1
    nb2 = float(input(f"Entrez le nombre numéro: {c}"))
    if nb2>maxi :
        maxi = nb2
        p=c
    sortir=input("Pour sortir de la boucle tapez 0 sinon tapez C pour continue:")
    if sortir=="0" :
        break
    elif sortir=="C" or sortir=="c" :
        continue
    else :
        continue
print(f"le max est {+maxi}, sa positon est {+c}")
#EXERCICE 6:
print("EXERCICE 6")
nb1 = float(input("Entrez un nombre:"))
s = 1
t = nb1
while nb1!=0 :
    nb2 = float(input("Entrez le nombre suivant"))
    s+=1
    t+=nb2
    sortir=input("Entrez 0 pour quitter la boucle sinon entrez C pour continue:")
    if sortir=='0' :
        break
    elif sortir=='C' or sortir=='c' :
        continue
    else :
        continue
print(f"la moyenne est, {t/s}")
#EXERCICE 1:
print("EXERCICE 1 LA SOMME")
x = float(input("Entrez la valeur de x:"))
n = int(input("Entrez la valeur finale de n:"))
while n<1 :
    n=int(input("la valeur doit etre suérieure ou égale à 1 Entrez une autre valeur :"))
s = 0
for i in range(1,n+1):
    S+=x**i
print("La somme est:",s)'''
#EXERCICE 2: Mot de passe
print("EXERCICE 2")
for i in range(3):
    mdp = input("Entrez le mot de passe correct : ")
    if mdp=="Bonjour" :
        break
if mdp=="Bonjour" :
    print("Authentification réussi")
else :
    rep = input("Entrez la réponse de question secret :")
    if rep=="Minou" :
        print("Authentification réussi")
    else :
        print("Votre compte est bloqué")
    
#EXERCICE 3 MINUTE ET SECONDE:
print("EXERCICE 3")
import time

m = int(input("Entrez la minute :"))
s = int(input("Entrez la seconde :"))

def compte_a_rebours(minutes, secondes):
    total_secondes = minutes * 60 + secondes
    for i in range(total_secondes, -1, -1):
        m = i // 60  
        s = i % 60
        print(f"{m}min : {s}sec")
        time.sleep(0.25)
        if m==00 and s==00 :
            break

compte_a_rebours(m, s)
################### METHODE 2 ##################
while True :
    print("Entrez un horraire :")
    min=int(input("minutes"))
    sec=int(input("secondes"))
    if min>=0 and min<60 and sec>=0 and sec<60 :
        break
while min!=0 or sec!=0 :
    if sec!=0 :
        sec-=1
    else :
        sec=59
        min-=1
    print(f"{min} : {sec}")
print("ARRET")
#EXERCICE 4:
nb=int(input("Entrez un nombre"))
nc=50
while nb!=nc :
    if nb > nc:
        nb=int(input("C'est plus, entrez un nombre correct :"))
    else :
        nb= int(input("C'est moins, entrez un nombre correct :"))
print(f"Félicitations ! Le nombre {nb} est correct.")
#EXERCICE 5 :
'''nb1=int(input("Entrez la valeur à rechercher :"))
f=0
for i in range(1,11) :
    nb2 = int(input(f"Entrez le nombre numéro {i} :"))
    if nb2==nb1 :
        f+=1
print("La valeur à rechercher apparait",f, "fois")'''



    

    



        






























            






















      

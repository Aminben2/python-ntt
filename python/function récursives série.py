'''def suite(nb):
    if nb==1 :
        return 1
    elif nb==2 :
        return 2
    else : 
        return suite(nb-1)*suite(nb-2)
# Programme principale
nb = int(input("Entrez un nombre :"))
p=1
for i in range(1,nb+1):
    print(f"U{i}={suite(i)}")
    p*=suite(i)
print("Le produit est :", p)'''
###################################Exercice fonction sur fonction######################
def somme(nb):
    s=0
    for i in range(1,nb+1):
        s+=i
    return s
nb=int(input("Entrez un nombre :"))
print(somme(nb))

#############deuxième fonction####################
def Exp(nb):
    E=0
    for i in range(1,nb+1):
        E+=1/somme(i)
    return E
print(Exp(nb))
######################### EXERCICE 8 ########################
def suite(N):
    if N==0:
        return 2
    elif N==1:
        return 3
    else :
        return (2/3*(suite(N-2)))-(1/4*(suite(N-1)))
N = int(input("Entrez un nombre :"))
if N==2 or N>100 :
    print("Erreur")
else :
    print(suite(N))



















        
        

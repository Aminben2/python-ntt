#EXERCICE 1 :
'''while True :
    n = int(input("Entrez la valeur de n :"))
    if n<=2 :
            print("le nombre est invalide")
    else :
        break
S1 = 1
S2 = 2
P = S1*S2
for i in range(1,n+1):
    if i==1 :
        print(S1)
    elif i==2 :
        print(S2)
    else :
        Sn= S1*S2
        print(Sn)
        P*=Sn
        S1, S2 = S2, Sn
print("Le produit des termes jusqua la limite :", P)'''

#EXERCICE 2 :
chaine1=input("entrez le chaine 1 :" )
chaine2=input("entrez le chaine 2 :" )
n1=0
n2=0
for i in chaine1 :
    n1+=1
for J in chaine2 :
    n2+=1
if n1!=n2 :
    print("les deux chaine pas anagrame ")
elif chaine1==chaine2 or chaine2==chaine1 :
    print("chaine 1 est anagramme de chaine 2")
else:
    B=0
    A=0
    for i in chaine1:
        for j in chaine2:
            if i==j:
                B+=1
                A+=1
    if B==A or A==B:
        print("chaine 1 est anagramme de chaine 2")
    else:
        print("chaine 1 n'est pas anagramme de chaine 2")
#EXERCICE 3:
'''while True :
    a= int(input("Entrez un nombre entier a :" ))
    if a>1 :
        break
while True :
    b=int(input("Entrez un nombre entier b :" ))
    if b>1 :
        break
sa=0
sb=0
for i in range(1,a):
    if a%i==0:
        sa+=i
for i in range(1,b):
    if b%i==0:
        sb+=i
if sa==b or sb==a :
    print(f"Les nombres {a} et {b} ce sont des nombres amis")
else :
    print(f"{a} et {b} ce sont des nombres pas amis")'''
        



























    

    
























            

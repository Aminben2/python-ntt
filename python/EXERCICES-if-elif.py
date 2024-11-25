#EXERCICE 1
print("EXERCICE 1")
a = float(input("Entrez le premier nombre :"))
b = float(input("Entrez le deuxième nombre :"))
c = float(input("Entrez le troisième nombre"))
import math
if a==0 :
    if b ==0 :
        print("Ce n'est pas une équation")
    else :
        print("X =", -c/b)
else :
    delta = (b**2)-(4*(a*c))
    if delta <0 :
        print("L'équation n'a pas de solution sur R")
    elif delta==0 :
        print("L'équation a une solution unique : X=", -b/(2*a))
    else :
        racine = math.sqrt(delta)
        solution1 = (-b-racine)/(2*a)
        solution2 = (-b+racine)/(2*a)
        print("Deux solutions sur R : X1 =", solution1, "et X2 =", solution2)
#EXERCICE 2
print("EXERCICE 2")
j = int(input("Entrez le jour:"))
m = int(input("Entrez le mois:"))
a = int(input("Entrez l'année:"))
if (j<1 or j>31 or m<1 or m>12 or a<1 or (j>28 and m==2) or (j>30 and (m==4 or m==6 or m==9 or m==11))):
    print("date invalide")
elif (j<28 and m==2)or(j<30 and(m==4 or m==6 or m==9 or m==11)or(j<31 and(m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12))): 
    print("la date est:", j+1,"/",m,"/",a)
elif (j==28 and m==2)or(j==30 and(m==4 or m==6 or m==9 or m==11)or(j==31 and(m==1 or m==3 or m==5 or m==7 or m==8 or m==10))): 
    print("la date est:", 1,"/",m+1,"/", a)
else :
    print("la date est:", 1,"/",1,"/", a+1)
#EXERCICE 3
print("EXERCICE 3")
ha = int(input("Entrez l'heure d'arrivee:"))
ma = int(input("Entrez la minute d'arrivee:"))
hd = int(input("Entrez l'heure de depart:"))
md = int(input("Entrez la minute de depart:"))
if hd>23 and md>59 or ha>23 and ma>59 or hd<0 and md<0 or ha<0 and ma<0 or (ha==hd and ma==md) :
    print("la duree invalide")
elif ha>=hd and ma>=md :
    print("L'heure est:", ha-hd,"h",ma-md,"m")
else :
    print("la duree est:", ha-hd-1,"h", ma-md+60,"m")
    if ma>=md :
        print("la duree est:", ha-hd+24,"h", ma-md,"m")
    else :
        print("la duree est:", ha-hd+24-1,"h",ma-md+60,"m")
#EXERCICE 4
print("EXERCICE 4")
m= float(input("Entrez un montant d'achat:"))
if m>5000 :
    print("la réduction et le montant à payer est:", m*0.2)
elif m>3000 and m<=5000 :
    print("la réduction et le montant à payer est:", m*0.15)
elif m>1000 and m<=3000 :
    print("la réduction et le montant à payer est:", m*0.1)
elif m<=0:
    print("montant d'achat invalide")
else :
    print("aucune réduction pur un montant d'achat inférieur à 1000dhs")
#EXERCICE 5
print("EXERCICE 5")
c = input("Entrez une catégorie de lecture (A,B,C) :")
no = int(input("Entrez le nombre d'ouvrage :"))
if c=="A" and no<5 :
    print("la duree d'emprunter = 20jrs et le droit d'emprunter = 1")
elif c=="B" and no<5 :
    print("la duree d'emprunter = 30jrs et le droit d'emprunter = 1")
elif c=="C" and no<5 :
    print("la duree d'emprunter = 45jrs et le droit d'emprunter = 1")
else :
    print("la duree et le droit d'emprunter est:", 0)

#méthode 2 exercice 2
'''print("méthode 2 exercice 2")
j = int(input("Entrer le jour:"))
m = int(input("Entrer le mois:"))
a = int(input("Entrer l'annee:"))
if (j<1 or j>31 or m<1 or m>12 or a<1 or (j>28 and m==2) or (j>30 and (m==4 or m==6 or m==9 or m==11))):
    print("date invalide")
else :
    #traitez les cas du mois
    if m==2 :
        nbj = 28
    elif m==4 or m==6 or m==9 or m==11 :
        nbj = '''
#EXERCICE 5 CORRECTION :
print("correction exercice 5")
nbo = int(input("Entrez le nombre d'ouvrages")
if 0<nbo>5 :
    cat = input("Entrez la categorie")
    if cat=="A" or cat=="a" :
          print("la duree est : 20jrs")
    elif cat=="B" or cat=="b" :
          print("la duree est : 30jrs")
    elif cat=="C" or cat=="c" :
          print("la duree est : 45jrs")
    else :
          print("categorie invalide")
elif nbo < 0 :
    print("nombre d'ouvrage invalide")
else :
    print("vous ne pouvez pas empruntez vous avez depasse le nmbre")

    





























#COURS FUNCTION :
#Définition : Exemple de foncton qui retourne un paramètre
'''def facto1(nb) : #paramètres formels/fictifs
    #corps de la fonction
    if nb==0 :
        return 1 #returrn arrete l'éxécution de la fonction
    
    f=1
    for i in range(1,nb+1):
         f*=i
    return f

N= int(input("Entrez un nombre :"))
res1 = facto1(N)    #N c'est un paramètre effectif

#function facto sans paramètre
def facto2() :
    nb=int(input("Entrez un nombre :"))
    if nb==0 :
        return 1 #returrn arrete l'éxécution de la fonction
    
    f=1
    for i in range(1,nb+1):
         f*=i
    return f

res2=facto2()
print("res facto1 :", res1 , "res facto2 :", res2)

#function = procédures : qui ne retourne rien
def comparaison(a,b,c) :
    if a==b==c :
        print(a,b,c, "sont égaux")
    elif a>=b and a>= c :
        print(a, "est le maximal")
    elif b>=a and b>= c :
        print(b, "est le maximal")
    else :
        print(c, "est le maximal")

comparaison(3,7,8)'''

#Appel des arguments  par les mots_clé:
#affichage(age=56,nom="ahmadi",prénomn="ahmed")

#Appel par position et mots_clé :
#somme(3,2,1,e=6,d=2) #regle = il faut commencer par les arguments positionnels ensuit

#Ladéclaration de la valeur par défaut pour les arguments:

def somme(a=1,b=1,c=1,d=1,e=1):
    print(f"{a}+{b}+{c}+{d}+{e}={a+b+c+d+e}")
somme()

#Les variables locales : les variables qui sont déclarées et utilisées au sein de la fonction
#et qui sont non reconnues par le programme principale (en dehors de la fonction)
#EXEMPLE :
def isprime(x):
    global F #Pour modifier la valeur de F(globale au sein de la fonction) on utilise global
    F="bbbbbb" #declaration d'une nouvelle F (variable locale)
    if x==0 or x==1 :
        return False
    nbdiv=0 #variable locale
    for i in range(2,x):
        if x%i==0:
            nbdiv+=1
            print("dans la fonction", nbdiv)
    return nbdiv==0
F="aaaaa" #variable globale
print(isprime(int(input("Entrez un nombre :"))))

#Variables globales : les variables qui sont déclarées dans le programme principale et elles peuvent etre utilisees partout



































#FOR LOOP :
#la fonction range(1-3 arguments entiers) : génére une liste des entiers
#range with 1 argument : range(vf): génére une liste starts from 0 ends at vf-1 with step 1
#for example : range(4) : [0,1,2,3]
#range with 2 argument : range(vi , vf) : générer une liste starts from vi  ends at vf-1 with a step 1
#range with 3 argument : range (vi , vf , step d) : générer une liste starts from vi ends at vf-1 with a step d
#range(3,9,3) : [3,6]
#cas pas positif : Vi < Vf
#cas pas négatif : Vi > Vf
#for loop 1 : with range()
'''for i in range(5) :     #   for in [0,1,2,3,4]:
    print("HELLO")'''
#EXERCICE 1
'''print("Exercice 1")
nb = int(input("Entrez le nombre:"))
print("Table de:", nb)
for i in range(1,11) :
    print(nb,"*",i, "=", nb*i)
#EXERCICE 2 :
print("Exercice 2")
nb = int(input("Entrez le nombre:"))
if nb<=0 :
    print("nombre invalide")
else :
    s=0
    for i in range(0,nb+1) :
        s+=i #s=s+i
        if i != nb :
            print(i,"+",end="")
        else :
            print(i,end="")
    print("=", s)
#EXERCICE 3:
nb = int(input("Entrez le nombre:"))
if nb<0 :
	input("on ne peut pas calculer le factoriel")
elif nb==0 :
	print("le factoriel de 0 est: 1")
else :
        f=1
        for i in range(1,nb+1) :
              f=f*i
        print("la factorielle est:", f)
# EXERCICE 3
nb = int(input("Entrez le nombre:"))
if nb<0 :
	input("on ne peut pas calculer le factoriel")
elif nb==0 :
	print("le factoriel de 0 est: 1")
else :
        f=1
        c=""
        for i in range(1,nb+1) :
            f*=i
            if i!= nb :
                c+=str(i)+"x"
            else :
                c+= str(i)
        print(c,"=",f)
#EXERCICE 4 :
print("exercice 4")
m=665
for i in range(1,11) :
    nb=float(input("Entrez un nombre"))
    if i==1 '''
###########################################
#la boucle for avec les chaines des caractères (string)
'''for i in "HELLO" :
    print(i)
print(i)'''
################################################
#le mot cle break: sort immediatement de la boucle
#exemple
for i in range(10) :
    print("hello")
    if i==4:
        print("by")
    break
print("on est apres la boucle")

























        




    


    

    



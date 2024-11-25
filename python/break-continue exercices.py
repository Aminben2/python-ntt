#Exercice 1 :
print("exercice1")
for i in range(0,10) :
    if i%2 !=0 :
        print(i)
    continue
#Exercice 3 :
print("exercice 3")
email = input("Entrez votre email")
p=""
for i in email :
    if i=="@" :
        break
    else :
        print(i,end="")

    
    

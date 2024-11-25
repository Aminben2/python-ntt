#Méthode 1
"""
car = ord(input("Entrez le caractere: "))
if ord("a") <= car and ord("z") >= car:
    print("Le caractere est minuscule")
elif ord("A") <= car and ord("Z")>= car:
    print("Le caractere est majuscule")
else:
    print("C'est un symbole")
"""
#Méthode 2
car = input("Entrez le caractere: ")
if car  >= "0" and car <= "9":
    print ("Numero")
elif car >= "a" and car <= "z":
    print("Minuscule")
elif car >= "A" and car <= "Z":
    print("Majuscule")
else: 
    print("Symbole")

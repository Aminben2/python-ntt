# Python
choix = 2
while choix != 3:
    print("""----- Menu ----
            1- Entrez a et b
            2- Afficher le produit des nombre entre a et b
            3- Quitter 

            Tapez votre choix
    """)
    choix = input()
    if choix == "1":
        a = int(input("Entrez a: "))
        b = int(input("Entrez b: "))
        while b <= a:
            b = int(input("Entrez b: "))
    elif choix == "2":
        if a is None and b is None:
            print("Vous devez entrer a et b: ")
        else:
            p = 1
            if b-a == 1:
                print("Le produit est 0")
            else:
                for i in range(a+1, b):
                    p *= i
                print("Le produit est: ", p)
    elif choix == "3":
        print("Merci")
    else:
        print("Invalide!")


# Algorithme menu
# Variables choix,a,b,i,P: entier
# Debut
# test <-- Faux
# 	Ecrire("------menu------")
# 	Ecrire("1- Entrez a et b")
# 	Ecrire("2- Affichez le produit des nombres entre a et b")
# 	Ecrire("3- Quitter")
# 	Ecrire("Tapez votre choix")
# 	Lire(choix)
# 	Selon choix
# 		cas 1 : Ecrire("Entrez a:")
# 				Lire(a)
# 				Répeter
# 					Ecrire("Entrez b: ")
# 					lire(b)
# 				Jusqua b>a
# 				test <-- Vrai
# 		cas 2 : Si test = Faux Alors
# 					Ecrire("a et b n'ont pas été saisi, choisissez 1")
# 				Sinon
# 					Si b-a = 1 Alors
# 						Ecrire("Le produit est 0")
# 					Sinon
# 						P <-- 1
# 						Pour i <-- a à b pas 1
# 							p <-- P * i
# 						FinPour
# 						Ecrire("Le produit est: ", P)
# 					FinSi
# 				FinSi
# 		cas 3 : Ecrire("Merci")
# 		autrement : Ecrire("Choix invalide")
# 	Jusqua choix = 3
# Fin

#######GESTION DES FICHIERS#####################
#Methode open() : pour ouvrir un fichier

#en peut ouvrir un fichier en :
#mode "r" = Read (le fichier doit etre existe déjà)
#mode "a" = Append (modifier la fin du fichier, et ouvrir le fichier)
#mode "w" = Write (ouvrir un fichier pour le modifier, créer le fichier s'il n'existe pas)
#mode "x" = Create (créer une nouveau fichier, retourne erreurs si le fichier existe déjà)
#mode d'écriture:
# "t" = pour ecrire un texte
# "b" = pour ecrire un binaire

#Syntaxe pour l'ouverture d'un fichier:
#f=open("Nomdufichier.txt") #le fichier doit etre trouver au meme endroit
#f=open("NomFichier.txt", "rt") = ouvrir le fichier en mode lecture "r" et mode lecture de text "t"
#Si le fichier n'existe pas sur le meme dossir de code python il doit donnez le chemin du fichier

#Exemple lecture d'un fichier:
'''demofile.txt
Hello! welcome to demofile.txt
This file is for testing purposes.
GOOD LUCK!'''
f=open("demofile.txt", "r")
print(f.read()) #Pour lire tout le texte
print(f.read(5)) #Pour lire les 5 premiers lettres
print(f.readline()) #lecture ligne par ligne
#Pour la lecture ligne par ligne en utilise autre manière:
f=open("demofile.txt", "r")
for i in f:
    print(i) #i prend les lignes


#methode close():
f=open("demofile.txt", "r")
print(f.read())
f.close()

#Exemple d'écriture d'un fichier:
f=open("demofile2.txt", "a")
f.write("Now the file has more content")
f.close()
print()
#open and read the file after the appending:
f=open("demofile2.txt", "r")
print(f.read())

#function write : Pour écrire ou modifier un fichier
#function read : Pour lire le fichier

#Pour la suppression d'un fichier en utilise:
#La méthode remove
'''import os
os.remove("demofile.txt")'''

'''import os
if os.path.exists("demofile.txt"): #return True or False
    os.remove("demofile.txt")
else :
    print("The file does not exist")
'''
#Pour supprimer un dossier
#methode os.rmdir(NomDossier)
'''import os
os.rmdir("monDossier")'''



#Exercice :
def Compteur_Mots(fichier):
    occ=0
    for i in fichier:
        mot=i.split() # Divise la ligne en une liste de mots
        for j in mot :
            if j=="Hello":
                occ+=1
    return occ
with open("demofile2.txt", "r") as f:
    print(Compteur_Mots(f))
                










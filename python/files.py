#gestionnaires  des fichiers textuelles .text
#ouverture d'un fichier : avec functuion open (chemin(r/a), mode_ouverture)
f=open('C:\\Users\\HP\\Desktop\\LES COURS\\JOUWAYREYA\\files.txt')
""".\\dos1\\test1.txt"""
print(f)
#lecriture /ecriture
f.close()
#utre methode
#with open('C:\\Users\\HP\\Desktop\\LES COURS\\JOUWAYREYA\\files.txt') as f
#les chemin relative :
"""
la meme dosie de programme ou en d'autre dosier parents ou grandes parents
"""   
#mode ouverture:
#r :read only => lecture seulement si le fichier n'existe pas une exception est declenchee
#w : write only => ecriture seulement , si le fichier n'existe pas ila va cree et ecrase tout contenu qui existe deja
#aappend=>ecriture seulemt mais il vas ajouter a continue qui exite deja 
#r+ : read and write 
#w+ : read and write (ecrasser le continue qui exicte deja  )
#a+ :  write 
#f=open("files.txt","r+")# chemin relatif
#les methode de lecture :
# file.read() => retourne le contenu sous forme d'un string (chaine )
#print(f.read())
#print(f.readlines())#retoyurne le contune de forme liste
#print(f.readline())#retourn une seul ligne selpn la posittion de curseure 
#lecriture
"""
f.close()
#read line avec boucles for
import os
print(os.path.getsize("files.txt"))
for i in (os.path.getsize("files.txt")):
    print(f.readline(),end="")
f.close()
#read line avec boucle
while f.tell()!= (os.path.getsize("files.txt")):
    print(f.readline(),end="")
#iteration derecte sure le fichier
for i in f :
    print(i,end="")
"""
#ecriture
#methode file.write
#f=open("files.txt", "a+")
#f.writelines("Woops! I have deleted the content!")
#f.close()
ventes={"Dupont":14, "Hervy":19, "Geoffroy":15, "Layec":21}
f=open("files.txt", "a+")
for i,j in ventes.items():
    f.write(f"{i}=>{j} \n")
f.close()



Produits = {"p1_563": ["lait",12.3,14,63], "p2_897": ["yaourt",2.3,3,200], "p1_563":
["jus",5,6.3,80]}
f=open("files.txt", "a+")
for i,j in Produits.items():
        f.write(f"code de produi est : {i}\n\tnom :{j[0]}\n\t prix d'achat{j[1]}\n\tprix de ventes{[2]}")
f.close()

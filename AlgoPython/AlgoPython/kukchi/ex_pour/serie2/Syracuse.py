
Un = int(input("Entrer le 1er nombre de la suite: "))
i = -1
while (Un > 1):
  if (Un % 2 == 0):
    Un = Un / 2
  else:
    Un = Un * 3 + 1

  i += 1
  print(f"U{i} = {int(Un)}")

'''
Algorithme Syracuse
Variables Un, i: entier
Debut
  Ecrire("Entrer le 1er nombre de la suite: ")
  lire(Un)
  i <- -1
  tantque Un > 1 faire
    si Un % 2 = 0 alors
      Un = Un / 2
    sinon
      Un = Un * 3 + 1
    i <- i + 1
    ecrire("U", i ,"=", Un)
'''
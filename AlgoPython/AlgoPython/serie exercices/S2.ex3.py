Un = int(input("Entrez le 1st nombre de la suite: "))
i = -1
while (Un > 1):
    if (Un % 2 == 0):
        Un = Un // 2
    else:
        Un = Un * 3 + 1
    i += 1
    print(f"U{i} = {int(Un)}")

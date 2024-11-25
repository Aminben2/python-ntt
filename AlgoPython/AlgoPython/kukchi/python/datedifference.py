print("Entrez le 1ere date")
j, m, a = int(input("(jour): ")), int(input("(Mois): ")), int(input("(Ans): "))

print("\nEntrez le 2eme date")
jj, mm, aa = int(input("(jour): ")), int(input("(Mois): ")), int(input("(Ans): "))

if ((j < 1 or j > 31) or (m<1 or m>12) or (a < 0) or (m == 2 and j>28 and not((a % 4 == 0 and a % 100 != 0) or (m == 2 and j>29 and (a % 4 == 0 and a % 100 != 0)) or (a % 400 == 0))) or (m == 4 or m == 6 or m == 9 or m == 11 and j>30)) and ((jj < 1 or jj > 31) or (mm<1 or mm>12) or (aa < 0) or (mm == 2 and jj>28 and not((aa % 4 == 0 and aa % 100 != 0) or (mm == 2 and jj>29 and (aa % 4 == 0 and aa % 100 != 0)) or (aa % 400 == 0))) or (mm == 4 or mm == 6 or mm == 9 or mm == 11 and jj>30))  :
    print("Date invalide")
else:
	if ((j == jj) and (m == mm) and (a == aa)) :
		print("les dates sont égaux")
	elif aa > a or ( aa == a and mm > m) or (aa == a and mm == m and jj > j):
		print("2eme date > 1ere date")
	else:
		print("1ere date > 2eme date")
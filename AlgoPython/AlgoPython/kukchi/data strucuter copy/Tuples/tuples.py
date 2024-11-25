t = [[5,2,4],[8,1,3],[3,9,7]]

for i in t:
	for j in i:
		print(j, end=" ")
	print()

for i in range(len(t)):
	for j in range(len(t[i])):
		print(t[i][j], end=" ")
	print()


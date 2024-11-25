# def gen_pyramide(n):
# 	for i in range(n):
# 		for j in range(i, n):
# 			print(" ", end="  ")
# 		for k in range(i):
# 			print("*", end="  ")
# 		for l in range(i+1):
# 			print("*", end="  ")
# 		print()
# 	print()

# gen_pyramide(int(input("entrer le nombre de lignes: ")))

def gen_pyramide(n):
	for i in range(n):
		for j in range(i, n):
			print(" ", end="  ")
		for k in range(i*2+1):
			print("*", end="  ")
		print()
	print()

gen_pyramide(int(input("entrer le nombre de lignes: ")))
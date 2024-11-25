nb = int(input())
# for i in range(1,11):
# 	print(f'{nb} x {i} = {nb*i}')

n = 1
for i in range(1, nb+1):
	n *= i
	print(f"{i}", end='*')
	

print(n)
		
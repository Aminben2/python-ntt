nums = list()
print('Entrer 10 nombres compris entre 0 et 20')
for i in range(10):
	userInput = int(input(f'Entrer le nombres {i+1}: '))
	while userInput > 20 or userInput < 0:
		userInput = int(input(f'Entrer le nombres {i+1}: '))
	nums.append(userInput)

print(nums)

for j in range(0, 21):
	# if nums.count(j) != 0:
	# 	print(f'le nombre {j} a tapé {nums.count(j)} fois')
	print(f'le nombre {j} a ete repeté {nums.count(j)} fois')
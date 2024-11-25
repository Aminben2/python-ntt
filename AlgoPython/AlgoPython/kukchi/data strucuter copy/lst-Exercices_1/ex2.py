N = int(input('entrer N: '))
numbers = list()
numbers.append(int(input('Entrer le nombre 1: ')))

maximum = numbers[0]
minimum = numbers[0]
posMax = 1
posMin = 1


counter = 1
for i in range(N-1):
	numbers.append(int(input(f'Entrer le nombre {counter+1}: ')))

	if maximum < numbers[i]:
		maximum = numbers[i]
		posMax = i+1

	elif minimum > numbers[i]:
		minimum = numbers[i]
		posMin = i+1

	counter += 1


# i = 1
# while True:
# 	userInput = input(f'Entrer le nombre {i+1}: ')

# 	if userInput.lower() == 'done':
# 		break
# 	else:
# 		numbers.append(int(userInput))

# 	if maximum < numbers[i]:
# 		maximum = numbers[i]
# 		posMax = i+1

# 	elif minimum > numbers[i]:
# 		minimum = numbers[i]
# 		posMin = i+1

# 	i += 1

print(f"Le plus grand de ces nombres est : {maximum}, sa position : {posMax}")
print(f"Le plus petit de ces nombres est : {minimum}, sa position : {posMin}")





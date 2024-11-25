
a = [5

, 3, -5, 1, 7]

somme = 0
for i in a:
	somme += i
print('Sum: ',somme)

maximum = a[0]
for i in a:
	if maximum < i:
		maximum = i
print('Max: ',maximum)

minimum = a[0] 
for i in a:
	if minimum < i:
		minimum = minimum
	else:
		minimum = i 
print('Min: ',minimum)






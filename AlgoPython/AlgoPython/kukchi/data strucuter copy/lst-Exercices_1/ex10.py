nums = list()
n = int(input('Entrer Combien des nombres: '))
if n <= 50:
	for i in range(n):
		userInput = int(input('Entrer une nombres: '))
		nums.append(userInput)
print(nums)

TPOS = []
TNEG = []

for i in nums:
	if i >= 0:
		TPOS.append(i)
	else:
		TNEG.append(i)

print(f'TPOS : {TPOS}\nTNEG : {TNEG}')






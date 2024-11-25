nums = list()
n = int(input('Entrer Combien des nombres: '))
if n <= 50:
	for i in range(n):
		userInput = int(input('Entrer une nombres: '))
		nums.append(userInput)

print(nums)
noZero = []
for i in nums:
	if i != 0:
		noZero.append(i)
nums = noZero
print(nums)


zeros = nums.count(0)
for i in range(zeros):
	nums.remove(0)
print(nums)


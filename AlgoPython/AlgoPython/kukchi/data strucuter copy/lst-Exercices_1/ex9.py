nums = list()
n = int(input('Entrer Combien des nombres: '))
if n <= 20:
	for i in range(n):
		userInput = int(input('Entrer une nombres: '))
		nums.append(userInput)
print(nums)

for i in range(int(len(nums) / 2)):
	n = nums[i]
	nums[i] = nums[-1 * (i + 1)]
	nums[-1 * (i + 1)] =  n

print(nums)
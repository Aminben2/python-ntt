l = [5,6,3,6,2,6,1,11,2,6,11,3,11,5,11,2,11,11,11,9,9,9]

print(f'la liste est:\n{l}')
# print(len(l))
# print(len(l) - l.count(9))

def maxRemover(lst):
	maxNum = max(lst)
	print(f'\nle max est {maxNum}')
	while maxNum in lst:
		lst.remove(maxNum)
	return lst


print(maxRemover(l))
# print(len(l))

def maxRemoverV2(lst ):
	maxNum =  max(lst)
	print(f'\nle max est {maxNum}')
	NumOfMax = lst.count(maxNum)
	for i in range (NumOfMax):
		lst.remove(maxNum)
	return lst

print(maxRemoverV2(l))

  


 
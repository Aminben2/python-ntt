tab1 = [1, 23, 6, 9, -1, 11]
tab2 = [2, 24, 6, 10, 0, 10]

nTab = []
for i in range(len(tab1)):
	nTab.append(tab1[i] + tab2[i])
	# nTab.insert(i, tab1[i]+tab2[i])

print(nTab)
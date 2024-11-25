# #Method 1
L = [4,6,1,7,1,6,9,2]
# print(L)
# minn = L[0]
# for i in range(len(L)):
# 	if L[i] <= minn:
# 		minn = L[i]
# 		posmin = i

# L[0], L[posmin] = L[posmin], L[0] 

# print(L)

# Method 2

L = L.reverse()
L[-1], L[L.index(min(L))] = L[L.index(min(L))], L[-1]

L = L.reverse()
def letterCounter(s):
	string = list(s)

	dict_chain = dict()
	for i in string:
		dict_chain[i] = dict_chain.get(i, 0) + 1

	

	return dict_chain

print(letterCounter('yusuf'))

# method 
# for i in string:
	# 	if i in dict_chain:
	# 		dict_chain[i] = dict_chain[i] + 1
	# 	else:
	# 		dict_chain[i] = 1

# method 2
def Nb_occ(s):
	d={}
	for i in s:
		Nb_occ = s.count(i)
		d.update({i:Nb_occ})
	return d
print(Nb_occ('yusuf'))



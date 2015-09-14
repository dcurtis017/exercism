def distance(strand1, strand2):
	list1 = list(strand1)
	list2 = list(strand2)
	counter = 0
	for i in range(0, len(list1)):
		if list1[i] != list2[i]:
			counter+=1
	return counter
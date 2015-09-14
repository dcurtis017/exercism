def sum_of_multiples(max_num, factors=[3,5]):
	return sum(list(filter(lambda x: len(list(filter(lambda y: y!= 0 and x%y == 0, factors))) > 0, list(range(1, max_num)))))
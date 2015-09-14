def sieve(maxNumber):
	counter = 2
	possibleNumbers = list(range(2, maxNumber+1))
	while(counter <= maxNumber):
		if counter in possibleNumbers:
			possibleNumbers = list(filter(lambda x: x == counter or x%counter != 0, possibleNumbers))
		counter+=1;
	return possibleNumbers
	

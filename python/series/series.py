def slices(digits, length):
	digits_len = len(digits)
	if length == 0 or length > digits_len:
		raise ValueError("The length specified must be greater than 0 and less than the length of the string provided")
	else:
		index = 0
		series = []
		check_len = digits_len-length
		while index <= check_len:
			series.append(list(map(lambda x: int(x), list(digits[index:(index+length)]))))
			index+=1
	return series

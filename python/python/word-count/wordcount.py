def word_count(str):
	words = {}
	for w in str.split():
		#if len(w.strip()) == 0:
		#	continue
		if not w in words:
			words[w] = 1
		else:
			words[w] = words[w]+1
	return words
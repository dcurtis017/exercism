def detect_anagrams(base_word, string_words):
	base_word_chars = sorted(list(base_word), key=lambda s: s.lower())
	anagrams = []
	#print(base_word_chars)
	for word in string_words:
		match = True
		if len(base_word) == len(word) and base_word.lower() != word.lower():
			tmp_chars = sorted(list(word), key=lambda s: s.lower());
			#print(tmp_chars)
			for index, val in enumerate(base_word_chars):
				if tmp_chars[index].lower() != val.lower():
					match = False
					break
			if(match):
				anagrams.append(word)
	return anagrams


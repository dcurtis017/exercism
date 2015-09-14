import re
from string import ascii_lowercase

def generate_keyring(encoding=True):
	return dict(zip(ascii_lowercase, ascii_lowercase[::-1]))
	
def encode(phrase):
	keyring = generate_keyring(True)
	rx = re.compile(r'[.?!,\s]')
	phrase = rx.sub('', phrase.lower())
	offset, encoded = 0, []
	for i in list(range(0, len(phrase))):
		encoded.append(keyring[phrase[i]] if phrase[i] in keyring else phrase[i])
		offset+=1
		if offset == 5:
			encoded.append(' ')
			offset = 0
	return ''.join(encoded).strip()
	
def decode(phrase):
	keyring = generate_keyring(False)
	phrase = list(phrase.replace(' ', ''))
	return ''.join(list(map(lambda x: keyring[x], phrase)))


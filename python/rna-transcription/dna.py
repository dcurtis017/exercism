def to_rna(dna):
	complements = {'G':'C', 'C':'G', 'T':'A', 'A':'U'}
	return ''.join(map(lambda x: complements[x], list(dna)))
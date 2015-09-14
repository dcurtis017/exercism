class Allergies:
	
	allergy_list = {128:'cats', 64: 'pollen', 32:'chocolate', 16:'tomatoes', 8:'strawberries', 4: 'shellfish', 2: 'peanuts', 1:'eggs'}

	def __init__(self, allergy_score):
		self.allergy_score = allergy_score
		self.lst = []
		if allergy_score > 0:
			self.find_allergies()
		
	def find_allergies(self):
		vals = sorted(list(Allergies.allergy_list.keys()), reverse=True)
		allergy_score = self.allergy_score
		for d in vals:
			if allergy_score >= d:
				allergy_score-=d
				self.lst.append(Allergies.allergy_list[d])
				if allergy_score == 0:
					break
	
	def is_allergic_to(self, allergy):
		return allergy in self.lst
		
#not sure what the extra credit test is actually trying to accomplish				
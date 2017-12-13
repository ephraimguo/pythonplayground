class SweetPotato:
	def __init__(self):
		self.doness = 0
		self.cookedStatus = 'raw'
		self.ingradient = []


	def __str__(self):
		return 'the sweet potato cooking process'

	
	def cook(self, time, ):
		self.doness += time
		#cook the sweetpotato
		if self.doness > 8:
			self.cookedStatus = 'overcooked'
		elif self.doness >5:
			self.cookedStatus = 'well done'
		elif self.doness >3:
			self.cookedStatus = 'medium well'
		else:
			self.cookedStatus = 'raw'




potato = SweetPotato()

print(potato.doness)
print(potato.cookedStatus)
print(potato.ingradient)

potato.cook(5)

print(potato.cookedStatus)


potato.cook(2)
print(potato.cookedStatus)


















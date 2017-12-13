class SweetPotato:
	def __init__(self):
		self.doness = 0
		self.cookedStatus = 'raw'
		self.ingradient = []


	def __str__(self):
		#msg = 'ur potato is at XXXX status, added ingradient is YYYY'
		msg = 'ur potato is at '+ self.cookedStatus + ' status '
		if len(self.ingradient)>0:
			msg += 'and ingradient added is '
			for temp in self.ingradient:
				msg = msg + temp + ', '
			msg = msg.strip(', ')
			
		return msg




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

	def addIngdt(self, ingdt):
		self.ingradient.append(ingdt)


potato = SweetPotato()

print(potato.doness)
#print(potato.cookedStatus)
print(potato)

print('----baked 5min----')
potato.cook(5)
#print(potato.cookedStatus)
print(potato)

print('----baked 2 more min----')
potato.cook(2)
#print(potato.cookedStatus)
print(potato)

print('---add ketchup-----')
potato.addIngdt('ketchup')
print(potato)

print('---add wasabi----')
potato.addIngdt('wasabi')
print(potato)


print('---bake 2 more min---')
print('----add chilli source----')
potato.cook(2)
potato.addIngdt('chilli')
print(potato)















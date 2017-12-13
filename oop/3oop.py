class Dog:

	def __init__(self, weight, color, name):
		self.weight = weight
		self.color = color	
		self.name = name

	def __str__(self):
		return 'this is puppy'




	def bark(self):
		print('wong wong wong')
	

	def run(self):
		print('dog is running')


	def eat(self):
		print('eating')
		#edit attribute inside the function
		self.weight += 5 


	def printName(self):
		print('Name is %s'%self.name)	



myDog = Dog(50,'cyan','XXXDDD')
#myDog.printName()
#print(myDog.color)
#print(myDog.weight)

print('*'*30)

wangcai = Dog(25,'mix','DDEEERRR')
#print(wangcai.color)
#print(wangcai.weight)
#wangcai.printName()

print(myDog)





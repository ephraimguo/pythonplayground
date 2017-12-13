class Dog:
	def bark(self):
		print('wong wong wong')
	def run(self):
		print('dog is running')

	def eat(self):
		print('eating')
		#edit attribute inside the function
		self.weight += 5 


myDog = Dog()
myDog.run()
myDog.bark()

myDog.color = 'yellow'
myDog.weight = 10

print(myDog.color)
print(myDog.weight)


myDog.eat()
print(myDog.weight)




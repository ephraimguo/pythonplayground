import sys
import pygame
def fibonacci(n): 
	a, b, counter = 0, 1, 0
	while True: 
		if counter > n:
			return
		yield a
		a, b = b, a+b
		counter += 1
f = fibonacci(int(input('key in the number u wan')))

while True:
	try:
		print(next(f),end=' ')
	except StopIteration:
		print('')
		sys.exit()

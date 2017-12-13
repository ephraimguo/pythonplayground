import os
import os.path

with open('test.txt') as test:
	readTxt = read(test.txt, delimiter=', ')
	
	for row in readTxt:
		print(row)

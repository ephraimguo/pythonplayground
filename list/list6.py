fileNames = ['01.txt','02.html','guoyanyu.doc','linlin.py','drive.exe']
name = input('pls key in the file name: ')
found = 0

for temp in fileNames:
	if temp == name:
		found = 1
		break
	else:
		found = 0 

if found == 1:
	print('found the file')
else:
	print('didnt found')
	
print('*'*30)

if name in fileNames:
	print('found')

else:
	print('NNNOOOOOO')	

fileName = ['01.py','02.txt','03.rar','04.c','05.cpp','06.php','07.java','index.html','final.doc']

for i in range(0,len(fileName)):
	tempName = fileName[i]

	position = tempName.rfind('.')

	print(tempName[position:])

print('*'*30)

i = 0
length = len(fileName)
while i<length:
	tempName=fileName[i]
	position = tempName.rfind('.')
	print(tempName[position:])
	i+=1

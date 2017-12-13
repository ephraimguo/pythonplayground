fileNames = ['01.txt','02.html','guoyanyu.doc','linlin.py','drive.exe']

for name in fileNames:
	print(name)


print('*'*30)

del fileNames[2]


for name in fileNames:

	print(name)
print('*'*30)
fileNames.pop()


for name in fileNames:

	print(name)
print('*'*30)

fileNames.remove('linlin.py')
for name in fileNames:
	print(name)
print('*'*30)

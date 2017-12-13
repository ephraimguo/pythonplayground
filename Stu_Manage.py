stuList = []


def funcList():
	print('*'*30)
	print('1. Add New ')
	print('2. Remove')
	print('3. Edit')
	print('4. Search')
	print('5. Transverse')
	print('6. Exit the system')
	print('*'*30)

def funcSearch(name):
	index_stu = stuList.index(name)
	return index_stu

def funcAdd():
	stuName = input('key in the student name: ')
	stuAge = int(input('key in the sutdent age: '))
	stuId = input('key in the student id: ')
	stuInfo = {}
	stuInfo['Name'] = stuName
	stuInfo['Age'] = stuAge
	stuInfo['StuId'] = stuId
	stuList.append(stuInfo)

def funcDel():
	num = int(input('Key in the index number you want to delete'))
	del stuList[num-1]

def trans():
	print('<>'*30)
	print('Id      Name      Age')
	for temp in stuList:

		print('%s    %s     %d'%(temp['StuId'],temp['Name'],temp['Age']))

	print('<>'*30)
def funcMain(numSelect):
	if numSelect == 1:
		funcAdd()	
	elif numSelect == 2:
		funcDel()
	elif numSelect == 3:
		pass
	elif numSelect == 4:
		pass
	elif numSelect == 5:
		trans()
	elif numSelect == 6:
		print('Exit the Sytem')
	else:
		print('invalid input')

i = 1
while i<10: 
	funcList()

	numSelect = int(input('key in the selection number'))

	funcMain(numSelect)
	if numSelect == 6:	
		quitConfirm = input('yes or no')
		if quitConfirm == 'yes':
			break

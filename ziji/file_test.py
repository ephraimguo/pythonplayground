import os
import os.path


#path = '/usr/local/Cellar/python3/3.6.3/Frameworks/'

ls = []

def getAppointFile(path, ls):
	try:
		for temp in fileList:
			pathTmp = os.path.join(path,tmp)
			if True == os.path.join(pathTmp):
				getAppointFile(pathTmp, ls)
			elif pathTmp[pathTmp.rfind('.')+1:].upper()=='py':
				ls.append(pathTmp)
	except PermissionError as msd:
		print(msg)

def main():

	while True:
		path = input('pls key in the path').strip()
		if os.path.isdir(path) == True:
			break
	
	getAppointFile(path, ls)
	print(ls)
	print(len(ls)

main()

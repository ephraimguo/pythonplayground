def find_start_imooc(f_name):

	f = open(f_name)
	for line in f:
		if line.startswith('imooc'):
			print(line)




def find_in_imooc(f_name):

	f = open(f_name)
	for line in f:
		if line.startswith('imooc') and line.endswith('imooc\n'):
			print(line)

find_in_imooc('imooc.txt')




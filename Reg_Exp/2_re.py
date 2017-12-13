import re
file_name = 'imooc.txt'

f = open(file_name)

pa = re.compile(r'imooc', re.I)

for line in f:
	mt = pa.match(line)

	print(mt)



	

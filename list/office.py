import random

office = [[],[],[]]

teacher = ['aaa','bbb','ccc','ddd','eee','fff','ggg','hhh']

#i = random.randint(0,2)

for k in teacher:
	office[random.randint(0,2)].append(k)
	for temp in office:
		print(temp)
	print('-'*20)
print('*'*30)
print(office)

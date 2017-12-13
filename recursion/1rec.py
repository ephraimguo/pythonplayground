 # recursion of function, a function embedded itself and loop

#def test1(num):
#	res = 0
#	i = 1 
#	while i<=num:
#		res+=i
#		i+=1
#	return res
#a = test1(100)
#print(a)

def test2(num):
	if num>1:
		res = num + test2(num-1)
	else:
		res = 1


test2(5)

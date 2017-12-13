def func_Factorial(num):
	if num > 1:
		res = num * func_Factorial(num-1)
		print('num = %d'%num)
		print('res = %d'%res)
	else:
		res = 1
	return res

a = func_Factorial(int(input('number')))
print(a)

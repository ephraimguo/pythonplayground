import time

def test1():
	num = 100
	print(num)

def test2():
	num = 100
	print(num)
	time.sleep(1)
	print(num*2)

test1()

time.sleep(1)

test2()

def test(first, *args):
	print('Required argument: %d' %first )
	for num in args:
		print('Optional argument: %d' %num)

test(123445)

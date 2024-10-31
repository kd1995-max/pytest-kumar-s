def test_argstest01(cmdopt):
	# print("Read config file: " + cmdopt.readline())
	assert cmdopt.readline().index('Lab')

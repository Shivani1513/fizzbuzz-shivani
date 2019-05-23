def fizzie(threes):
	while threes<100:
		threes = threes+1
		if ((threes%3==0) & (threes%5==0)):
			print("fizzbuzz")
		elif (threes%3==0):
			print("fizz")
		elif (threes%5==0):
			print("buzz")
		else:
			print(threes)
fizzie(0) 


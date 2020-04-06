def check_two(x):
	return ((x != 0) and ((x & (~x + 1)) == x)) #the power of 2 shows the position of "1" bit
	#return x > 0 and (x & (x - 1)) == 0

print(check_two(1))

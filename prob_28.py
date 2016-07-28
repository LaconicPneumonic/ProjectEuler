f_sum = 1
rows = 1001
for num in xrange(3,rows +1 , 2):
	f_sum += 4* (num ** 2) - 6*(num - 1)

print f_sum
n = 2
for i in xrange(7830456):
	n *= 2
	n %= 10 ** 10
	#Only need to multiply last ten numbers
n = n * 28433
n += 1

print n % 10 ** 10
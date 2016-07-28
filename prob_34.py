import math
f_sum = 0 

for i in xrange(3 ,50000):
	t_sum = 0
	i =str(i)
	for a in i:
		t_sum += math.factorial(int(a))
	if t_sum == int(i):
		print i
		f_sum += t_sum

print f_sum
f_sum = 0 

for i in xrange(2 ,354294):
	t_sum = 0
	i =str(i)
	for a in i:
		t_sum += int(a) ** 5
	if t_sum == int(i):
		print i
		f_sum += t_sum

print f_sum
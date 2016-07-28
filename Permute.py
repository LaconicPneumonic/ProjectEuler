sum = 0
lst = []

for a in xrange(1,10):
    for b in xrange(10):
        for c in xrange(10):
            d = str(a) + str(b) + str(c) + str(b) + str(a)
            lst.append(d)
            sum += int(c)

print sum * 100
print len(lst)

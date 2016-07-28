sum = 0
S1 = 0
S2 = 0
S3 = 0
S4 = 0
S5 = 0
lst = []

for a in xrange(1,10):
    for b in xrange(10):
        for c in xrange(10):
            d = str(a) + str(b) + str(c) + str(b) + str(a)
            lst.append(d)
            S1 += (a*10000)
            S2 += (b*1000)
            S3 += (c*100)
            S4 += (b*10)
            S5 += (a)

            sum += int(d)

print sum
print S1,S2,S3,S4,S5
print len(lst)


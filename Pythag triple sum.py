for i in xrange(1,1000):
    for a in xrange(1,1000):
        b = (((i ** 2 + a ** 2) ** .5))
        if b % 1 == 0:
            sum = a + i + b
            if sum == 1000:
                print a*i*b
                break




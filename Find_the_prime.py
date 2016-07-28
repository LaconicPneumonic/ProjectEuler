n = 2
i = 0

limit = raw_input("Which prime do you want to find?")

while not limit.isdigit():
    limit = raw_input("Out of index try again.")

limit = int(limit)

primes = []

while True:
    b = int(n ** .5 + 1)
    for x in xrange(2, b):
        if n % 2 == 0 and n != 2:
            break
        elif n % x == 0 and n != 2:
            break
    else:
        # loop false without finding a factor
        i+=1
        if i == limit:
            prime = n
            break
    n += 1

limit = float(limit)
ratio = float((limit -1)/prime) * 100.0

print "%d is the %dth prime" % (prime,limit)
print "{} percent of the numbers below {} are prime".format(ratio,prime)

def sum_primes_under(limit):
    n = 2
    add = 0
    while True:
        b = int(n ** .5 + 1)
        for x in xrange(2, b):
            if n % 2 == 0 and n != 2:
                break
            elif n % x == 0 and n != 2:
                break
        else:
            # loop false without finding a factor
            if n <= limit:
                add += n
            else:
                return add
                break

        n += 1

print sum_primes_under(int(raw_input("I will find the sum of primes under a number of your choosing")))
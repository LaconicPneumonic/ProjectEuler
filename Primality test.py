def is_prime(x):
    if x < 2:
        return False
    for i in xrange(2,int(x**.5 +1)):
        if x % i == 0:
            return False

    return True

def primality(limit):
    primes = []
    for a in xrange(limit):
        if is_prime(a):
            primes.append(a)
    return primes

print primality(104743)



primes = []
cool = []
top = int(raw_input("Smallest number divisible by 1 through: 'What number?'"))
n = 2
while True:
    b = int(n ** .5 + 1)
    for x in xrange(2, b):
        if n % 2 == 0 and n != 2:
            break
        elif n % x == 0 and n != 2:
            break
    else:
        # loop false without finding a factor
        # Found Prime!
        if n <= top:
            primes.append(n)
        else:
            break

    n += 1

for a in primes:
    for i in xrange(1, top + 1):
          if a ** i >= top:
              cool.append(a ** (i -1))
              break

sum = 1

for c in cool:
    sum *= c

print sum

a = 0
for i in str(sum):
    a += 1
print "there are",a,"digits in this number"
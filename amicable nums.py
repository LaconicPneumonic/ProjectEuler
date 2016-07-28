def prop_div(num):
    n = int(num ** .5)
    divs = ""
    for i in xrange(2,n+1):
        if num % i == 0:
            divs += " %d %d" % (i, num/i)

    return divs

def add(n):
    divisors = prop_div(n).split(" ")
    divisors.append(1)
    divisors.pop(0)
    sum = 0
    for i in divisors:
        sum += int(i)
    return sum

def amiccable(num):
    a = add(num)
    if num == add(num):
        return False
    elif num == add(a):
        return True
    else:
        return False

sum = 0
for i in xrange(1,10000):

    if amiccable(i):
        sum += i

print sum



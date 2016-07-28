a = 60

def Collatz(n):
    i = 1
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n /= 2
        else:
            n = 3*n +1
        i += 1
    return i

def count(limit):
    i=1
    greatest = [(0,0)]
    values = []
    while i < limit:
        a = (Collatz(i),i)
        if a > greatest[0]:
            greatest[0] = a
        i += 1
    return greatest[0]

print count(1000000)



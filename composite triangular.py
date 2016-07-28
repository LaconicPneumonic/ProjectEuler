

def triangle_factors(num):
    i = 1
    while 1:
        tri = int((i **2 +i)/2) #calculaes ith triangular number
        factors = 0
        for d in xrange(1,int(tri**.5 + 1)):
            if a % d == 0:
                num += 2 # Every factor has a pair
        if factors > limit:
            break
        i+=1

    return a

print triangle_factors(500)




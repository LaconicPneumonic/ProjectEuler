import msvcrt as m
nums = []
for i in xrange(100,1000):
    for a in xrange(100,1000):
        b = str(a * i)[::-1]
        if int(str(a * i)) == int(b):
            nums.append((a * i,a,i))

print max(nums)

def wait():
    m.getch()
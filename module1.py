file = open('C:\\Users\\Anthony\\Desktop\\Programming\\num.txt', 'r')
a = file.read()


b = []
for i in xrange(1,101):
    b.append(a[(i-1)*50:i*50])

sum = 0
for i in b:
    sum += int(i)

print str(sum)[:10]
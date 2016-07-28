names = open("p042_words.txt","r").read().split(",")
alfa_to_num = {
	"\"" :0,
	"A":1,
	"B":2,
	"C":3,
	"D":4,
	"E":5,
	"F":6,
	"G":7,
	"H":8,
	"I":9,
	"J":10,
	"K":11,
	"L":12,
	"M":13,
	"N":14,
	"O":15,
	"P":16,
	"Q":17,
	"R":18,
	"S":19,
	"T":20,
	"U":21,
	"V":22,
	"W":23,
	"X":24,
	"Y":25,
	"Z":26
}

def summ(word):
	sm = 0
	for i in word:
		sm += alfa_to_num[i]
	return sm

def triag_check(num):
	n = ((1 + 8.0 * num) ** (1/2.0) - 1) / 2.0
	return n % 1 == 0


def run():
	cnt = 0
	for name in names:
		if triag_check(summ(name)):
			print name , summ(name)
			cnt += 1
	return cnt

print run()










def read(num):
	lng = len(str(num))
	num = str(num)
	word = ""
	num_to_word = {
	0 : "", 
	1 : "one",
	2 : "two", 
	3 : "three",
	4 : "four",
	5 : "five",
	6 : "six",
	7 : "seven",
	8 : "eight",
	9 : "nine",
	10 : "ten",
	11 : "eleven",
	12 : "twelve",
	13 : "thirteen",
	14 : "fourteen",
	15 : "fifteen",
	16 : "sixteen",
	17 : "seventeen",
	18 : "eighteen",
	19 : "nineteen"

	}

	if lng == 4:
		word += num_to_word[int(num[0])] + " thousand "
		word += num_to_word[int(num[1])] + " hundred "
		if num[2] != "1":
		    word += num_to_word[int(num[2])] + "ty " + num_to_word[int(num[3])]
		else:
			word += num_to_word[int(num[2] + num[3])]
	elif  lng == 3:
		word += num_to_word[int(num[0])] + " hundred "
		if num[2] != "1":
		    word += num_to_word[int(num[1])] + "ty " + num_to_word[int(num[2])]
		else:
			word += num_to_word[int(num[1] + num[2])]
	elif lng == 2:
		if num[2] != "1":
		    word += num_to_word[int(num[0])] + "ty " + num_to_word[int(num[1])]
		else:
			word += num_to_word[int(num[0] + num[1])]
	else:
		word += num_to_word[int(num[0])]
	print word


	return word

print read(0512)


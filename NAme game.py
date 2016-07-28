my_file = open("C:\\Users\\Anthony\\Desktop\\names.txt",'r')

names = my_file.read().split(",")
new_names = []
for i in names:
    new_names.append(i[1:len(i)-1])
new_names.sort()

print new_names.index("COLIN")

sum = 0
prod = 0
for i in new_names:
    prod = 0
    for x in i:
        if x.lower() == "a":
            prod += 1
        elif x.lower() == "b":
            prod += 2
        elif x.lower() == "c":
            prod += 3
        elif x.lower() == "d":
            prod += 4
        elif x.lower() == "e":
            prod += 5
        elif x.lower() == "f":
            prod += 6
        elif x.lower() == "g":
            prod += 7
        elif x.lower() == "h":
            prod += 8
        elif x.lower() == "i":
            prod += 9
        elif x.lower() == "j":
            prod += 10
        elif x.lower() == "k":
            prod += 11
        elif x.lower() == "l":
            prod += 12
        elif x.lower() == "m":
            prod += 13
        elif x.lower() == "n":
            prod += 14
        elif x.lower() == "o":
            prod += 15
        elif x.lower() == "p":
            prod += 16
        elif x.lower() == "q":
            prod += 17
        elif x.lower() == "r":
            prod += 18
        elif x.lower() == "s":
            prod += 19
        elif x.lower() == "t":
            prod += 20
        elif x.lower() == "u":
            prod += 21
        elif x.lower() == "v":
            prod += 22
        elif x.lower() == "w":
            prod += 23
        elif x.lower() == "x":
            prod += 24
        elif x.lower() == "y":
            prod += 25
        elif x.lower() == "z":
            prod += 26
    prod *= new_names.index(i)+1
    sum += prod

print sum




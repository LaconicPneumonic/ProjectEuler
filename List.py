def sort_dis(a):
    empty_lst = []
    d = len(a)

    for l in xrange(d):
        b = 0

        for i in a:
            if i > b:
                b = i

        a.pop(a.index(b))
        empty_lst.append(b)

    a = []
    for i in empty_lst:
        a.insert(0,i)

    return a

print sort_dis([1,2098,3,84,5,6,45354,5,345,435,354,345,3,453,54,345,34,736,825,7,90,425,44,456,65,45,5,56,6,65,65,65,5454,4,5645,645,645,64])




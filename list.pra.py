def shuffle(l1, l2):
    l3 = []
    length1 = len(l1)
    length2 = len(l2)
    for i in range(len(l1+l2)):
        if length1 != 0:
            l3.append(l1[i])
            length1 -= 1
        if length2 != 0:
            l3.append(l2[i])
            length2 -= 1
    return l3


print(shuffle([0, 2, 4], [1, 3, 5]))
print(shuffle([0, 2, 4], [1]))
print(shuffle([0], [1, 3, 5]))

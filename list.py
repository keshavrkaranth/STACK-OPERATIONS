# list_1 =[0]
# list_2=[1,3,5]
# list_3=sorted(list_1+list_2)
#
# print(list_3)
l1=[0]
l2=[2,4,6,8]
def suffix(l1,l2):
    l3=[]
    for i in range(len(l1+l2)):
        l3.append(l1[i-len(l2)])
        l3.append(l2[i-len(l1)])
    return list(dict.fromkeys(l3))



print(suffix(l1,l2))
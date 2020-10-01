# BinarySearch
lst = [2, 4, 5, 8, 9, 12, 14, 17, 20]
length = len(lst)
key = int(input("plz enter the key: "))
lb = 0
ub = length-1
while(lb<=ub):
    mid = (lb+ub)//2
    if(key==lst[mid]):
        print("element found")
        break
    elif(key<lst[mid]):
        ub = mid-1
    else:
        lb = lb+1
if(lb>ub):
    print("element not found")


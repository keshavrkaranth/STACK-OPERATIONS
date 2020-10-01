import itertools
list1=map(int,input().split())
list2=map(int,input().split())
for i in itertools.product(list1,list2):
    print(i,end="")
# from itertools import product
#
# A = map(int,input().split())
# B = map(int,input().split())
#
# for item in product(A,B):
#     print(item,end=' ')

# def product(ar_list):
#     if not ar_list:
#         yield ()
#     else:
#         for a in ar_list[0]:
#             for prod in product(ar_list[1:]):
#                 yield (a,)+prod
#
# print(list(product([[1,2],[3,4],[5,6]])))
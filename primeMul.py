def primeproduct(n):
    out = list()
    if(n>0):
        for num in range(1, n+1):
            prime = True
            for i in range(2, num):
                if (num % i == 0):
                    prime = False
            if prime:
                out.append(num)
        for i in range(1,len(out)):
            for j in range(1,len(out)):
                if ((out[i] * out[j]) == n):
                    return True
    return False
print(primeproduct(188))
print(primeproduct(6))
print(primeproduct(202))
print(primeproduct(-6))


# n = int(input("Enter a prime num: "))
# k = primes_method1(n)
# print(k)

# def checkprime(lis,num):
#     for i in lis:
#         for j in lis:
#             if((i*j)==num):
#                 return True
#     return False
#
# print(checkprime(k,n))
#

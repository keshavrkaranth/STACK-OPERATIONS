# fibinocci
length = int(input("enter the sequence length"))
f1 = 0
f2 = 1
count = 2
print('fibinocci no are')
print(f1)
print(f2)
while(count<=length):
    fib3 =f1+f2
    print(fib3)
    # f1 = f2
    # f2 = fib3
    f1,f2 = f2,fib3
    count+=1

array = []
sum = 0
no_of_elements=int(input("Enter the number of elements: "))
print("Enter the Elements one by one: ")
for i in range(no_of_elements):
    k = input()
    array.append(k)
for j in array:
    sum = sum+int(j)
print(f"The sum of array elemmets is: {sum}")
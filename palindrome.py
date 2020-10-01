input_string = input("Enter the string to check the palindrome: ")
temp = input_string
if(temp[::-1] != input_string):
    print(f"Enterd String {input_string} is not a palindrome")
else:
    print(f"Enterd String {input_string} is a palindrome")

print("Do you want to see palindromed string type y to see:")
display_palinrome = input()
if(display_palinrome == "y"):
    print(temp[::-1])
else:
    print("THANK YOU")

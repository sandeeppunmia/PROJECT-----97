# 2. To find if the given number is prime or not.

number = int(input("Enter any number:- "))

for i in range(2,number):
    if(number % i == 0):
        print("The given number is not prime")
        break
    else:
        print("The given number is prime")
        break 
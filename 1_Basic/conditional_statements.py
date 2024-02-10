''' 
if statement
if-else statement
if-elif-else statement
nested if-else statement
'''

number = int(input("Enter a number: "))

#if statement
if number>0:
    print("This is a positive number")


#if-else statement
if number % 2 == 0:
    print("The number is even")
else:
    print("The number is odd")



#if-elif-else statement
if number > 10:
    print("The number is greater than 10")
elif number == 10:
    print("The number is equal to 10")
else:
    print("The number is less than 10")



#nested if statement
if number > 0:
    if number % 5 == 0:
        print("The number is positive and divisible by 5")



'''
OUTPUT:

Enter a number: 85
This is a positive number
The number is odd
The number is greater than 10
The number is positive and divisible by 5

'''
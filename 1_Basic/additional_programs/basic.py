'''#program to find the square root of a number

x = int(input("Enter a number: "))
ans = x**0.5
print(ans)

'''

'''#program to find area of Rectangle
l=5
b=6
rect = l*b
print(rect)'''


#pattern program
# 1234
# 123
# 12
# 1

'''a=[1,2,3,4]
for i in range(4+1):
    for j in range(4-i):
        print(a[j], end=" ")
    print(" ")


'''

#program which finds sum of digits of a number
'''
x = int(input("Enter a number: "))
tot=0
while(x>0):
    dig = x%10
    tot = tot+dig
    x=x//10
print(tot)'''

'''#cal surface volume and area of cylinder
p = 3.14
h = 4
r = 6
vol = p*r*r*h
s=((2*p*r)*h)+((p*r*2)*2)
print("volume : ",vol)
print("surface area: ", s)
'''

#program to reverse a given number
n=int(input("enter a number: "))
sum = 0
while(n!=0):
    r=n%10
    sum=(sum*10)+r
    n=n//10
print("reverse: ", sum)

'''Iteration 1:
r = 5, sum = 5, n = 1234
Iteration 2:
r = 4, sum = 54, n = 123
Iteration 3:
r = 3, sum = 543, n = 12
Iteration 4:
r = 2, sum = 5432, n = 1
Iteration 5:
r = 1, sum = 54321, n = 0   '''

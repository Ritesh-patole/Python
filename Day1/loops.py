'''
while loop
for loop
nested loop

'''

#for loop
fruits = ['apple','banana','orange']
print("using for loop with list: ")
for fruit in fruits:
    print(fruit)


#for loop with range
print("\n using a for loop with range: ")
for i in range(1,10):
    print(i)



#while loop
print("\n using a while loop: ")
count = 0
while count < 5:
    print(count)
    count+=1


#nested loops
print("\n using nested loops: ")
for i in range(3):
    for j in range(2):
        print(f"({i}, {j})")
    


'''
Output: 

using for loop with list: 
apple
banana
orange

 using a for loop with range: 
1
2
3
4
5
6
7
8
9

 using a while loop: 
0
1
2
3
4

 using nested loops: 
(0, 0)
(0, 1)
(1, 0)
(1, 1)
(2, 0)
(2, 1)

'''
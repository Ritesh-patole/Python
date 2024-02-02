
# Creating Lists
empty_list = []
mixed_list = [1, 'apple', 3.14, True]
nested_list = [[1, 2, 3], ['a', 'b', 'c']]
list2=['sky', 'moon', 'land', 'tree']

# Accessing Elements
first_element = mixed_list[0]
last_element = mixed_list[-1]
sublist = mixed_list[1:3]

# Modifying Lists
mixed_list.append('orange')
mixed_list.insert(1, 'banana')
removed_element = mixed_list.pop(2)
mixed_list[0] = 42

# List Methods
length = len(mixed_list)
sorted_list = sorted(list2)
index_of_3_14 = mixed_list.index(3.14)
count_of_apple = mixed_list.count('apple')

# List Operations
combined_list = mixed_list + ['grape', 'kiwi']
repeated_list = [1, 2] * 3

# Checking Membership
is_in_list = 'banana' in mixed_list

# Iterating through a List
print("\nIterating through a list:")
for element in mixed_list:
    print(element)
print("\n")
# List Comprehension
squared_numbers = [x**2 for x in range(5)]

# Displaying Results
print("empty_list:", empty_list)
print("mixed_list:", mixed_list)
print("nested_list:", nested_list)
print("first_element:", first_element)
print("last_element:", last_element)
print("sublist:", sublist)
print("removed_element:", removed_element)
print("length:", length)
print("sorted_list:", sorted_list)
print("index_of_3_14:", index_of_3_14)
print("count_of_apple:", count_of_apple)
print("combined_list:", combined_list)
print("repeated_list:", repeated_list)
print("is_in_list:", is_in_list)
print("squared_numbers:", squared_numbers)



'''Output: 

Iterating through a list:
42
banana
3.14
True
orange

empty_list: []
mixed_list: [42, 'banana', 3.14, True, 'orange']
nested_list: [[1, 2, 3], ['a', 'b', 'c']]
first_element: 1
last_element: True
sublist: ['apple', 3.14]
removed_element: apple
length: 5
sorted_list: ['land', 'moon', 'sky', 'tree']
index_of_3_14: 2
count_of_apple: 0
combined_list: [42, 'banana', 3.14, True, 'orange', 'grape', 'kiwi']
repeated_list: [1, 2, 1, 2, 1, 2]
is_in_list: True
squared_numbers: [0, 1, 4, 9, 16]
'''
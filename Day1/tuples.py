
# Creating Tuples
empty_tuple = ()
single_element_tuple = (42,)  # Note the comma for a single-element tuple
fruit_tuple = ('apple', 'banana', 'cherry')
nested_tuple = ((1, 2), ('a', 'b'))

# Accessing Elements
first_element = fruit_tuple[0]
last_element = fruit_tuple[-1]
subtuple = fruit_tuple[1:3]

# Tuple Unpacking
first, second, third = fruit_tuple

# Modifying Tuples (Note: Tuples are immutable, so modification involves creating a new tuple)
modified_tuple = fruit_tuple + ('orange', 'grape')

# Tuple Methods
length = len(fruit_tuple)
index_of_cherry = fruit_tuple.index('cherry')
count_of_banana = fruit_tuple.count('banana')

# Checking Membership
is_in_tuple = 'apple' in fruit_tuple

# Iterating through a Tuple
print("Iterating through a tuple:")
for item in fruit_tuple:
    print(item)

# Displaying Results
print("empty_tuple:", empty_tuple)
print("single_element_tuple:", single_element_tuple)
print("fruit_tuple:", fruit_tuple)
print("nested_tuple:", nested_tuple)
print("first_element:", first_element)
print("last_element:", last_element)
print("subtuple:", subtuple)
print("first:", first)
print("second:", second)
print("third:", third)
print("modified_tuple:", modified_tuple)
print("length:", length)
print("index_of_cherry:", index_of_cherry)
print("count_of_banana:", count_of_banana)
print("is_in_tuple:", is_in_tuple)




# Creating a tuple
my_tuple = (10, 20, 30, 'apple', 'banana', 'cherry')

# Accessing elements using indexing
print("First element:", my_tuple[0])  # Output: 10
print("Fourth element:", my_tuple[3])  # Output: 'apple'

# Concatenating tuples
another_tuple = ('dog', 'elephant', 'fox')
combined_tuple = my_tuple + another_tuple
print("Combined tuple:", combined_tuple)
# Output: (10, 20, 30, 'apple', 'banana', 'cherry', 'dog', 'elephant', 'fox')

# Using a function with tuples
def display_tuple_info(t):
    print("Length of the tuple:", len(t))
    print("Is 'apple' in the tuple?", 'apple' in t)

# Calling the function with our tuple
display_tuple_info(my_tuple)

# Using a tuple method
index_of_banana = combined_tuple.index('banana')
print("Index of 'banana':", index_of_banana)
# Output: Index of 'banana': 4




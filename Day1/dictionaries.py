# Creating Dictionaries
empty_dict = {}
fruit_dict = {'apple': 3, 'banana': 5, 'cherry': 2}
nested_dict = {'person': {'name': 'Alice', 'age': 25}, 'location': {'city': 'Wonderland', 'country': 'Fictionland'}}

# Accessing Values
apple_quantity = fruit_dict['apple']
nested_age = nested_dict['person']['age']

# Modifying Dictionaries
fruit_dict['orange'] = 4
fruit_dict.update({'banana': 8, 'grape': 6})
removed_value = fruit_dict.pop('cherry', None)

# Dictionary Methods
keys_list = list(fruit_dict.keys())
values_list = list(fruit_dict.values())
items_list = list(fruit_dict.items())

# Checking Membership
is_in_dict = 'apple' in fruit_dict

# Iterating through a Dictionary
print("Iterating through a dictionary:")
for key, value in fruit_dict.items():
    print(f"{key}: {value}")

# Dictionary Comprehension
squared_values = {key: value**2 for key, value in fruit_dict.items()}

# Displaying Results
print("empty_dict:", empty_dict)
print("fruit_dict:", fruit_dict)
print("nested_dict:", nested_dict)
print("apple_quantity:", apple_quantity)
print("nested_age:", nested_age)
print("removed_value:", removed_value)
print("keys_list:", keys_list)
print("values_list:", values_list)
print("items_list:", items_list)
print("is_in_dict:", is_in_dict)
print("squared_values:", squared_values)

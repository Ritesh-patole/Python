#Arithmetic Operators  +, - , *, /, %, Exoinent ** , Floor Division //
#Comparison/Relational Operators 
#Assignment Operators
#Logical Operators
#Bitwise Operators
#Membership Operators
#Identity Operators

num1=10
num2=20

add = num1+num2
sub = num1-num2
mul = num1*num2
div = num1/num2
module = num1%num2
exp = num1**num2

#comparison
equal = num1==num2
not_equal = num1!=num2
greater_than = num2 > num1
less_than = num2 < num1
greater_than_equal = num1 >= num2
less_than_equal = num1 <= num2

#logical
logical_and = True and False
logical_or =  True or False
logical_not = not True

#Bitwise
Bitwise_and = num1 & num2
Bitwise_or = num1|num2
Bitwise_xor = num1^num2
Bitwise_not_num1 = ~num1
left_shift = num1 << 2
right_shift = num1 >> 2

#Membership
list = [1,2,3,4,5]
is_in_list = 3 in list
not_in_list = 6 not in list

#identity operators
x=10
y=10
z=[10]

is_same_object = x is y
is_not_same_object = x is not y
is_same_value_but_diff_object = x == z[0]


#display results
print("Arithemetic operator = ", add, mul, div, module,exp,)
print("")
print(f"Arithmetic operators: {add}, {sub}, {mul}, {div}, {module}, {exp}")
print(f"Comparison operators: {equal}, {not_equal}, {greater_than}, {less_than}, {greater_than_equal}, {less_than_equal}")
print(f"Logical operators: {logical_and}, {logical_or}, {logical_not}")
print(f"Bitwise operators: {Bitwise_and}, {Bitwise_or}, {Bitwise_xor}, {Bitwise_not_num1}, {left_shift}, {right_shift}")
print(f"Membership operators: {is_in_list}, {not_in_list}")
print(f"Identity operators: {is_same_object}, {is_not_same_object}, {is_same_value_but_diff_object}")





# Output - 
# Arithmetic operators: 30, -10, 200, 0.5, 10, 100000000000000000000
# Comparison operators: False, True, True, False, False, True
# Logical operators: False, True, False
# Bitwise operators: 0, 30, 30, -11, 40, 2
# Membership operators: True, True
# Identity operators: True, False, True
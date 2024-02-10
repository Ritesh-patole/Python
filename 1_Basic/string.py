'''
Accessing characters
Strings Methods
formatting strings
string operations


'''

single_quoted_string = 'hello, world!'
double_quoted_string = "Python programming"
multiline_string = """ this is a 
multiline string.."""
concatenated_string = single_quoted_string + ' ' + double_quoted_string

#accessing characters
first_char = single_quoted_string[0]
last_char = single_quoted_string[-1]
substring = single_quoted_string[3:12]

#sting methods
length = len(single_quoted_string)
uppercase_string = single_quoted_string.upper()
lowercase_string = single_quoted_string.lower()
index_of_comma = single_quoted_string.find(',')
replaced_string = single_quoted_string.replace('hello', 'python')


#formatting stings
name = 'Alice'
age = 23
formatted_string = f"my name is {name} and my age is {age}"
formatted_string2 = "my name is {} and i am {} years old.".format(name,age)

#string operations
repeated_string = 'abc'*3



#display result
print("Single quoted string: ", single_quoted_string)
print("Double quoted string: ", double_quoted_string)
print("Multiline string: ", multiline_string)
print("Concatenated string: ", concatenated_string)
print("First char: ", first_char)
print("Last char: ", last_char)
print("Substring: ", substring)
print("length: ", length)
print("Uppercase: ", uppercase_string)
print("lowercase: ", lowercase_string)
print("index of comma: ", index_of_comma)
print("replaced string: ", replaced_string)
print("formatted string: ", formatted_string)
print("formatted string 2: ", formatted_string2)
print("repeated string:", repeated_string)



'''Output : 

Single quoted string:  hello, world!
Double quoted string:  Python programming
Multiline string:   this is a 
multiline string..
Concatenated string:  hello, world! Python programming
First char:  h
Last char:  !
Substring:  lo, world
length:  13
Uppercase:  HELLO, WORLD!
lowercase:  hello, world!
index of comma:  5
replaced string:  python, world!
formatted string:  my name is Alice and my age is 23
formatted string 2:  my name is Alice and i am 23 years old.
repeated string: abcabcabc

'''


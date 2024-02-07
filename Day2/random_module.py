import random

# randrange(start, stop[, step])
print("randrange Example:")
random_number = random.randrange(1, 10, 2)
print(random_number)

# shuffle(list)
print("\nshuffle(list) Example:")
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print(my_list)

# uniform(a, b)
print("\nuniform(a, b) Example:")
random_float = random.uniform(1.0, 5.0)
print(random_float)

# random()
print("\nrandom() Example:")
random_float = random.random()
print(random_float)

# randint(a, b)
print("\nrandint(a, b) Example:")
random_integer = random.randint(1, 10)
print(random_integer)

# choice(seq)
print("\nchoice(seq) Example:")
my_sequence = ['apple', 'banana', 'orange', 'grape']
random_choice = random.choice(my_sequence)
print(random_choice)

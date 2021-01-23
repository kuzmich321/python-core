# We can think of variable equality in two fundamental ways:
# Memory Address AND Object State (data)


# Memory Address
# is (identity operator)
# var_1 is var_2
# var_1 is not var_2 OR not(var_1 is var_2)


# Object State
# == (equality operator)
# var_1 == var_2
# var_1 != var_2 OR not(var_1 == var_2)


# The None object can be assigned to variables to indicate that they are not
# set (in the way would expect them to be), i.e. an "empty" value (or null pointer)

# But the None object is a real object that is managed by the Python memory manager

# Furthermore, the memory manager will always use a shared reference when
# assigning a variable to None

# We can test if a variable is "not set" or "empty" by comparing it's memory
# address to the memory address of None using is operator

# Examples

a = 10
b = 10

print(a is b, a == b)

a = 500
b = 500

print(a is b, a == b)

print('--------')

a = 'hello'
b = 'hello'

print(a is b, a == b)  # Do not count on it

print('--------')

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b, a == b)

print('--------')

a = 10
b = 10.0

print(a is b)
print(a == b)

print('--------')

a = 10 + 0j
print(a is b, a == b)

print('--------')

a = None
b = None
c = 10

print(hex(id(a)), hex(id(b)))
print(a is None, c is None, c is not None)

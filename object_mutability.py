# Consider an object in memory {type, data}
# Changing the data inside the object is called modifying the internal state of the object

# Suppose we have my_account where class is BankAccount and its data
# account_number and balance. We can change the balance.
# Internal state (data) has changed. Memory address has not changed.
# Object was mutated (fancy way of saying the internal data has changed)

# An object whose internal state CAN be changed, is called Mutable
# An object whose internal state CANNOT be changed, is called Immutable

# Examples:

# Immutable
# Numbers (int, float, Booleans, etc)
# Strings
# Tuples
# Frozen Sets
# User-Defined Classes

# Mutable
# Lists
# Sets
# Dictionaries
# User-Defined Classes

# Warning
# Tuples are immutable: elements cannot be deleted, inserted, or replaced
# In this case, both the container (tuple), and all its elements are immutable
t = (1, 2, 3)

# Consider this
a = [1, 2]
b = [3, 4]
t = (a, b)

a.append(3)
b.append(5)

print(t)

# The object references in the tuple did not change
# but the referenced objects did mutate!

# The tuple is immutable but it can contain mutable objects
# Do not confuse immutability that is completely frozen that can never be changed


my_list = [1, 2, 3]
print(hex(id(my_list)))

my_list.append(4)
print(hex(id(my_list)))

print('---------')

my_list_1 = [1, 2, 3]
print(hex(id(my_list_1)))

my_list_1 = my_list_1 + [4]  # This was not modifying the internal state
print(hex(id(my_list_1)))

print('----------')

my_dict = {
    'key1': 1,
    'key2': 'a'
}

print(hex(id(my_dict)))

my_dict['key3'] = 10.5

print(my_dict)
print(hex(id(my_dict)))

print('----------')

my_tuple = (1, 2, 3)
print(hex(id(my_tuple[0])))
print(hex(id(my_tuple[1])))

my_tuple = ([1, 2], [3, 4])
my_tuple[0].append(3)
print(my_tuple)
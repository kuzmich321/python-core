# The term SHARED REFERENCE is the concept of two variables referencing
# the SAME object in memory (i.e. having the same memory address)

# a = 10 and b = a IS THE SAME AS a = 10 and b = 10
# s1 = 'hello' and s2 = s1 IS THE SAME AS s1 = 'hello' and s2 = 'hello'

# In both these cases, Python's memory manager decides to automatically re-use
# the memory references!!
# Is this even safe? YES

# When working with mutable objects we have to be more careful
# With mutable objects, the Python memory manager will never create shared references
# a = [1, 2, 3] and b = a IS NOT THE SAME AS a = [1, 2, 3] and b = [1, 2, 3]


s1 = 'hello'
s2 = s1

print(hex(id(s1)), hex(id(s2)))

s2 = 'hello  world'

print(hex(id(s1)), hex(id(s2)))

print('--------')

my_list1 = [1, 2, 3]
my_list2 = my_list1

print(hex(id(my_list1)), hex(id(my_list2)))

my_list2.append(4)

print(my_list1, my_list1)
print(hex(id(my_list1)), hex(id(my_list2)))

print('--------')

# Do not count on it!

a = 10
b = 10

print(hex(id(a)), hex(id(b)))

b = 12

print(hex(id(a)), hex(id(b)))

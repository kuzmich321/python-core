# Immutable objects are safe from unintended side-effects

# process() scope
def process(s):
    print(f"Initial s # = {hex(id(s))}")
    s = s + ' world'
    print(f"Final s # = {hex(id(s))}")
    return s


# Module scope
my_var = 'hello'


# We're passing my_var reference to function
# s (line 6**) is gonna create a new object 'hello world'
print(process(my_var))
print(my_var)


print('---------')

# Mutable objects are NOT safe from unintended side-effects


def modify_list(lst):
    print(f"Initial lst # = {hex(id(lst))}")
    lst.append(100)
    print(f"Final lst # = {hex(id(lst))}")


my_list = [1, 2, 3]

print(modify_list(my_list))
print(my_list)

print('---------')

# Immutable collection that contain mutable objects


def modify_tuple(t):
    print(f"Initial t # = {hex(id(t))}")
    t[0].append(3)
    print(f"Final t # = {hex(id(t))}")


my_tuple = ([1, 2], 'a')


print(modify_tuple(my_tuple), my_tuple)
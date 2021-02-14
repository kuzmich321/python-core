# PEP 285
# The bool class
# Python has a concrete <bool> class that is used to represent Boolean values.
# However, the <bool> class is a subclass of the <int> class
# i.e they posses all the properties and methods on integers, and add some specialized ones such as: and, or...

# Two constants are defined: True and False
# They are <singleton> objects of type <bool>

# is vs == ...
# Because True and False are singleton objects, they will always retain their same memory addresses
# throughout the lifetime of your app

# So, comparisons of any Boolean expression to True or False can be performed using either
# the is (identity) or == (equality) operators

# But since bool objects are also int objects, they can also be interpreted as the integers 1 and 0
# But! True and 1 are not the same objects
# id(True) != id(1)
# id(False) != id(0)

# The Boolean constructor: bool(x) returns True when x is True, and False when x is False
# Wow, that sounds like a useless constructor! But not at all!
# What really happens is that many classes contain a definition of how to cast instances of themselves to a Boolean -
# this is sometimes called the <truth value> (or truthyness) of an object
# Ex: Integers have a truth value defined according to this rule:
# bool(0) --> False
# bool(x) --> True for any int x != 0

print(issubclass(bool, int))
print(isinstance(True, bool))
print(isinstance(True, int))

print('------------------')

# You can do these weird things
print(True > False)
print((1 == 2) == False)
print((1 == 2) == 0)
print(True + True + True)
print((True + True + True) % 2)
print(-True)

print('------------------')

print(bool(0))
print(bool(1))
print(bool(100))
print(bool(-1))

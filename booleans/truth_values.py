# All objects in Python have an associated truth value
# In general, the rules are straightforward

# Every object has a True truth value, except:
# None
# False
# 0 in any numeric type (0, 0.0, 0+0j, ...)
# empty sequences (list, tuple, string, ...)
# empty mapping types (dictionary, set, ...)
# custom classes that implement a __bool__ or __len__ method that returns False or 0

# Under the hood
# Classes define their truth values by defining a special instance method:
# __bool__(self)    or     __len__
# Then, when we can bool(x) Python will actually executes x.__bool__()
# or __len__ if __bool__ is not defined
# if neither is defined, then True

# Ex: Integers
# def __bool__(self):
# return self != 0
# When we call bool(100) Python actually executes 100.__bool__()
# and therefore returns the result of 100 != 0 which is True

# if my_list IS THE SAME AS
# if my_list is not None and len(my_list) > 0

print(bool([1, 2, 3]))
print(bool([]))
print(bool(None))
print(bool('abc'))
print(bool(''))

a = [1, 2, 3]
if a is not None and len(a) > 0:
	print(a[0])
else:
	print('Nothing to see here...')

if a:
	print(a[0])
else:
	print('Nothing to see here...')

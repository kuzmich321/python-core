from datetime import datetime
from time import sleep

# What happens at run-time...
# When a module is loaded: all code is executed immediately

# Module Code
a = 10  # the integer object is created, and func references it


def func(a):  # the function object is created, and func references it
	print(a)


func(a)


# What about default values?
# the function object is created, and func references it and the int object 10 is created and assigned as default to a
def func(a=10):
	print(a)


# by the time this happens, the default value for a has already been evaluated and assigned -
# it is not re-evaluated when the function is called
func()


# Consider this:
def log(msg, *, dt=datetime.utcnow()):
	print(f"{dt}: {msg}")


log('message 1')

# sleep(10)

log('message 2')


# Solution Pattern
# We set a default dt to None
# Inside the function, we test to see if dt is still None
# if dt is None, set it to the current date/time
# otherwise, use what the caller specified for dt
def log(msg, *, dt=None):
	dt = dt or datetime.utcnow()
	print(f"{dt}: {msg}")


log('message 1')

# sleep(10)

log('message 2')


# !!! In general, always beware of using a mutable object (or a callable) for an argument default
my_list = [1, 2, 3]


def func(a=my_list):
	print(a)


func()
my_list.append(4)
func()

print('-------------------')


def add_item(name, quantity, unit, grocery_list=[]):
	grocery_list.append(f"{name} ({quantity} {unit})")
	return grocery_list


store1 = []
store2 = []

add_item('banana', 2, 'units', store1)
add_item('milk', 1, 'liter', store1)

print(store1)

add_item('python', 1, 'medium-rare', store2)

print(store2)

del store1
del store2

print('-------------------')

store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'liter', store1)
print(store1)

store2 = add_item('python', 1, 'medium-rare')
print(store2)
print(store1 is store2)

print('-------------------')


def add_item(name, quantity, unit, grocery_list=None):
	grocery_list = grocery_list or []
	grocery_list.append(f"{name} ({quantity} {unit})")
	return grocery_list


store1 = add_item('banana', 2, 'units')
add_item('milk', 1, 'liter', store1)
print(store1)

store2 = add_item('python', 1, 'medium-rare')
print(store2)
print(store1 is store2)

print('-------------------')


def factorial(n, *, cache={}):
	if n < 1:
		return 1
	elif n in cache:
		return cache[n]
	else:
		print(f"calculating {n}!")
		result = n * factorial(n - 1)
		cache[n] = result
		return result


cache = {}
print(factorial(3))
print(factorial(3))
print(factorial(4))

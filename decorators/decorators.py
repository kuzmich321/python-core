from functools import wraps

# Decorators
# In general a decorator function:
# - takes a function as an argument
# - returns a closure
# - the closure usually accepts any combination of parameters
# - runs some code in the inner function (closure)
# - the closure function calls the original function using the arguments passed to the closure
# - returns whatever is returned by that function call


# Decorators and the @ Symbol
def counter(fn):
	count = 0

	def inner(*args, **kwargs):
		nonlocal count
		count += 1
		print(f'{fn.__name__} has been called {count} times')
		return fn(*args, **kwargs)
	return inner


@counter
def add(a, b):
	return a + b


# is the same as writing
def add(a, b):
	return a + b


add = counter(add)


@counter
def mult(a, b, c=1):
	"""
		return the product of three values
	"""
	return a * b * c


print(mult.__name__)
help(mult)


# One approach to fixing this
# The functools.wraps function
# In fact, the wraps function is itself a decorator
# but it needs to know what was our "original" function - in this case fn
def counter(fn):
	count = 0

	@wraps(fn)
	def inner(*args, **kwargs):
		nonlocal count
		count += 1
		print(f'{fn.__name__} has been called {count} times')
		return fn(*args, **kwargs)
	return inner


@counter
def mult(a: int, b: int, c: int = 1):
	"""
		return the product of three values
	"""
	return a * b * c


mult(1, 2, 3)
print(mult.__name__)
help(mult)

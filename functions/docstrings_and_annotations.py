# Docstrings
# help(x) --> returns some documentation (if available) for x
# We can document out functions (and modules, classes, etc) to achieve the same result using docstrings --> PEP 257
# If the <first line> in the function body is a string (just string by itself), it'll be interpreted as a <docstring>
def my_func(a):
	"""
	documentation for my_func
	"""
	return a


help(my_func)

# Where are docstrings stored? Ine function's __doc__ property
print(my_func.__doc__)


# Function Annotations
# Function annotations give is an additional way to document our functions  --> PEP 3107
# Where are annotations stored?
# In the __annotations__ property of the function
# It's a dictionary. For a return annotation, the key is <return>

def my_func1(a: 'a string', b: 'a positive integer') -> 'a string':
	"""
	Returns a * b
	"""
	return a * b


help(my_func1)


# Annotations can be any expression

def my_func2(a: str, b: 'int > 0') -> str:
	return a * b


def my_func2(a: str, b: [1, 2, 3]) -> str:
	return a * b


help(my_func2)
print(my_func2.__annotations__)

# Where does Python use docstrings and annotations?
# It doesn't really! Mainly used by external tools and modules
# Example: apps that generate documentation from your code

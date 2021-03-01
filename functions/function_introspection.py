import inspect


# Functions are first-class objects
# They have attributes __doc__ __annotations__
# We can attach out own attributes
def my_func(a, b=2, c=3, *, kw1, kw2=2):
	pass


my_func.category = 'math'
my_func.sub_category = 'arithmetic'

print(my_func.category, my_func.sub_category)
print('-----------------------')

# The dir() function
# dir() is built in function that, given an object as an argument, will return a list of a valid attributes
# for that object

print(dir(my_func))

# Function Attributes: __name__, __defaults__, __kwdefaults__
print(my_func.__name__)
print(my_func.__defaults__)
print(my_func.__kwdefaults__)


# Function Attribute: __code__
def my_func(a, b=1, *args, **kwargs):
	i = 10
	b = min(i, b)
	return a * b


print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)
print('-----------------------')


# The inspect Module
def my_func(*args: 'add extra positional', **kwargs):
	pass


class MyClass:
	def func(self):
		pass


my_obj = MyClass()

print(inspect.isfunction(my_func), inspect.ismethod(my_func))
print(inspect.isfunction(my_obj.func), inspect.ismethod(my_obj.func))
print(inspect.isroutine(my_func), inspect.isroutine(my_obj.func))  # Function or Method

# We can recover the source code of out functions/methods
print(inspect.getsource(my_func))

# We can find out in which module out function was created
print(inspect.getmodule(my_func))
print(inspect.getmodule(print))

# We can get comments
print(inspect.getcomments(my_func))
print('-----------------------')

# Callable Signatures
for param in inspect.signature(my_func).parameters.values():
	print('Name:', param.name)
	print('Default:', param.default)
	print('Annotation:', param.annotation)
	print('Kind:', param.kind)
	print('-----------------------')


for param in inspect.signature(divmod).parameters.values():
	print(param.kind)
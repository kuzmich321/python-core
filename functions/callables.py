# What are callables?
# Any object that can be called using the () operator
# Callables always return a value
# like functions and methods. but it goes beyond just those two
# Many other objects in Python are also callable
# To see if an object is callable, we can use the built-in function: callable

# Different Types of Callables
# built-in functions
# built-on methods
# user-defined functions
# methods
# classes
# class instances --> if the class implements __call__ method
# generators, coroutines, asynchronous generators

print(callable(print))
print(callable('abc'.upper))
print(callable(str.upper))
print(callable(callable))

print(callable(10))


class MyClass:
	def __init__(self, x=0):
		print('initializing...')
		self.x = x

	def __call__(self, x=1):
		print('updating x...')
		self.x += x

	def get_x(self):
		return self.x


my_class_instance = MyClass(100)
print(callable(MyClass))
print(callable(my_class_instance))
print(callable(my_class_instance.get_x))
my_class_instance()
print(my_class_instance.x)

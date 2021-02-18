# Positional Arguments
# Most common way of assigning arguments to parameters: via the order in which they are passed
def my_func(a, b, c):
	print(f"a={a}, b={b}, c={c}")


my_func(1, 2, 3)
print('----------------')


# Default Values
# A positional arguments can be made <optional> by specifying a default value for the corresponding parameter
# If a positional parameter is defined with a default value <every> positional parameter after it
# must also be given a default value
def my_func(a=1, b=2, c=3):
	print(f"a={a}, b={b}, c={c}")


my_func(10, 20, 30)
my_func(10, 20)
my_func(10)
my_func()
print('----------------')


# But what if we want to specify the 1st and 3rd arguments, but omit the 2nd argument?
# i.e we want to specify values for a and c, but let b tale on its default value?

# Keyword Arguments (named arguments)
# Positional arguments can, optionally, be specified by using the parameter name
# whether or not the parameters have default values
# But once you use a named argument, all arguments thereafter must be named too
def my_func(a, b=2, c=3):
	print(f"a={a}, b={b}, c={c}")


my_func(c=30, b=20, a=10)
my_func(10, c=30, b=20)
my_func(10, c=30)

from functools import partial


# Reducing Function Arguments

def my_func(a, b, c):
	print(a, b, c)


def fn(b, c):
	return my_func(10, b, c)
fn(20, 30)


f = lambda b, c: my_func(10, b, c)
f(20, 30)


f = partial(my_func, 10)
f(20, 30)


# Handling more complex arguments
def my_func(a, b, *args, k1, k2, **kwargs):
	print(a, b, args, k1, k2, kwargs)


def f(b, *args, k2, **kwargs):
	return my_func(10, b, *args, k1='a', k2=2, **kwargs)


f = partial(my_func, 10, k1='a')


def my_pow(base, exponent):
	return base ** exponent


square = partial(my_pow, exponent=2)
cube = partial(my_pow, exponent=3)

print(square(5))
print(cube(5))
print(square(5, exponent=3))


# Beware!
# You can use variables when creating partials
# but there arises a similar issue to argument default values
def my_func(a, b, c):
	print(a, b, c)


a = 10
f = partial(my_func, a)
f(20, 30)
a = 100
f(20, 30)

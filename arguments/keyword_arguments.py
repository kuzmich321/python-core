# Mandatory Keyword Arguments
# We can make keyword arguments mandatory.
# To do so, we create parameters after the positional parameters have been exhausted
def my_func(a, b, *args, d):
	print(f"a={a} b={b} args={args} d={d}")


my_func(1, 2, 'x', 'y', d=100)
my_func(1, 2, d=100)


# We can even omit any mandatory positional arguments
def func(*args, d):
	print(f"args={args} d={d}")


func(1, 2, 3, d=100)
func(d=100)


# In fact we can force no positional arguments at all
# * indicates the "end" of positional arguments
def func1(*, d):
	pass


def func2(a, b, *, d):
	print(a, b, d)


# It fails
# func1(1, 2, 3, d=100)
func1(d=100)
func2(1, 2, d=3)

print('--------------')


def func(a, b=2, *args, d):
	print(a, b, args, d)


func(1, 5, 3, 4, d='a')


def func(a, b=20, *args, d=0, e):
	print(a, b, args, d, e)


func(5, 4, 3, 2, 1, e='xyz')
func(0, 600, d='lol', e='python')

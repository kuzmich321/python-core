# Recall: a, b, *c = 10, 20, 'a', 'b'   --> a=10, b=20, c=['a', 'b']
# Something similar happens when <positional> arguments are passed to a function
def my_func(a, b, *c):
	print(a, b, c)


my_func(10, 20, 'a', 'b')


# The * parameter name is arbitrary - you can make it whatever you want
# It's customary (but not required) to name it *args
def my_func(a, b, *args):
	print(a, b, args)


my_func(10, 20, 'a', 'b')

# *args exhausts positional arguments
# You cannot add more positional arguments after *args
# This will not work!
# def my_func(a, b, *args, d)


def my_func1(a, b, c):
	print(a, b, c)


l = [10, 20, 30]
my_func1(*l)


def avg(*args):
	count = len(args)
	total = sum(args)
	print((count and total/count))


avg(2, 2, 4, 4)
avg()


def avg(a, *args):
	count = len(args) + 1
	total = sum(args) + a
	print((count and total/count))


avg(2, 2, 4, 4)
# avg()

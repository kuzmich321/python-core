# *args is used to scoop up variable amount of remaining positional arguments   --> tuple
# **kwargs is used to scoop up variable amount of remaining keyword arguments   --> dictionary
# **kwargs can be specified even if the positional arguments have NOT been exhausted (unlike keyword-only arguments)
# No parameters can come after **kwargs

def func(*, d, **kwargs):
	print(d, kwargs)


func(d=1, a=2, b=3)
func(d=1)


def func(**kwargs):
	print(kwargs)


func(a=1, b=2, c=3)
func()


def func(*args, **kwargs):
	print(args, kwargs)


func(1, 2, a=10, b=20)
func()

# Recap

# positional arguments
# may have default values
# *args - collects, and exhausts remaining positional arguments + indicates the enf of positional arguments

# keyword-only  arguments
# after positional arguments have been exhausted
# may have default values
# **kwargs - collects any remaining keyword arguments

# a, b, c=10
# positional parameters
# can have default values
# non-defaulted params are mandatory
# user may specify them using keywords

# *args - scoops up any additional positional args
# * - indicated NO MORE positional arguments

# kw1, kw2=100
# specific keyword-only args
# can have default values
# non-defaulted params are mandatory
# user MUST specify them using keywords
# if used, * or *args must also be used

# **kwargs - scoops up any additional keyword args

def func(a, b=10):
	pass


def func(a, b, *args):
	pass


def func(a, b, *args, kw1, kw2=100):
	pass


def func(a, b=10, *, kw1, kw2=100):
	pass


def func(a, b, *args, kw1, kw2=100, **kwargs):
	pass


def func(*args):
	pass


def func(**kwargs):
	pass


def func(*args, **kwargs):
	pass


# Typical Use Cases:
# print() function

def calc_hi_lo_avg(*args, log_to_console=False):
	hi = int(bool(args) and max(args))
	lo = min(args) if args else 0
	avg = (hi + lo) / 2
	if log_to_console:
		print(f"high={hi}, low={lo}, avg={avg}")
	return avg


is_debug = True
avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=is_debug)

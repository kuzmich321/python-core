from .decorator_app_timer import timed

print('------------------')


def logged(fn):
	from functools import wraps
	from datetime import datetime, timezone

	@wraps(fn)
	def inner(*args, **kwargs):
		run_dt = datetime.now(timezone.utc)
		result = fn(*args, **kwargs)
		print(f'{run_dt}: called {fn.__name__}')
		return result

	return inner


@logged
def func_1():
	pass


@logged
def func_2():
	pass


func_1()
func_2()


@logged
@timed
def fact(n):
	from operator import mul
	from functools import reduce

	return reduce(mul, range(1, n+1))


fact(5)
print('------------------')


def dec_1(fn):
	def inner():
		print('Running dec_1')
		return fn()
	return inner


def dec_2(fn):
	def inner():
		print('Running dec_2')
		return fn()
	return inner


@dec_1
@dec_2
def my_func():
	print('Running my_func')


my_func()
print('------------------')


def dec_1(fn):
	def inner():
		result = fn()
		print('Running dec_1')
		return result
	return inner


def dec_2(fn):
	def inner():
		result = fn()
		print('Running dec_2')
		return result
	return inner


@dec_1
@dec_2
@logged
@timed
def my_func():
	print('Running my_func')


my_func()

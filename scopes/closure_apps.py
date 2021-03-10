from time import perf_counter


class Averager:
	def __init__(self):
		self.numbers = []

	def add(self, number):
		self.numbers.append(number)
		total = sum(self.numbers)
		count = len(self.numbers)
		return total / count


a = Averager()
a.add(10)
a.add(20)
print(a.add(30))
print('------------------------------')


def averager():
	numbers = []

	def add(number):
		numbers.append(number)
		total = sum(numbers)
		count = len(numbers)
		return total / count
	return add


a = averager()
a(10)
a(20)
print(a(30))
b = averager()
print(b(10))
print('------------------------------')


def averager():
	total = 0
	count = 0

	def add(number):
		nonlocal total
		nonlocal count
		total += number
		count += 1
		return total / count
	return add


a = averager()
a(10)
a(20)
print(a(30))
b = averager()
print(b(10))
print('------------------------------')


class Timer():
	def __init__(self):
		self.start = perf_counter()

	def __call__(self):
		return perf_counter() - self.start


t1 = Timer()
print(t1())
print('------------------------------')


def timer():
	start = perf_counter()

	def poll():
		return perf_counter() - start
	return poll


t2 = timer()
print(t2())
print('------------------------------')


def counter(initial_value=0):
	def inc(increment=1):
		nonlocal initial_value
		initial_value += increment
		return initial_value
	return inc


counter1 = counter()
print(counter1())
print('------------------------------')


def counter(fn):
	count = 0

	def inner(*args, **kwargs):
		nonlocal count
		count += 1
		print(f'{fn.__name__} has been called {count} times')
		return fn(*args, **kwargs)
	return inner


def add(a, b):
	return a + b


def mult(a, b):
	return a * b


counter_add = counter(add)
print(counter_add.__closure__)

result = counter_add(10, 20)
print(result)

counter_mult = counter(mult)
counter_mult(2, 5)
counter_mult(2, 5)
print('------------------------------')


counters = dict()


def counter(fn):
	cnt = 0

	def inner(*args, **kwargs):
		nonlocal cnt
		cnt += 1
		counters[fn.__name__] = cnt
		return fn(*args, **kwargs)
	return inner


counter_add = counter(add)
counter_mult = counter(mult)

counter_add(10, 20)
counter_add(20, 30)
counter_mult(2, 5)

print(counters)
print('------------------------------')


def counter(fn, counters):
	cnt = 0

	def inner(*args, **kwargs):
		nonlocal cnt
		cnt += 1
		counters[fn.__name__] = cnt
		return fn(*args, **kwargs)
	return inner


c = dict()

counter_add = counter(add, c)
counter_mult = counter(mult, c)

counter_add(10, 20)
counter_mult(20, 30)
counter_mult(2, 5)
print(counters)
print(c)
print('------------------------------')


def fact(n):
	product = 1
	for i in range(2, n+1):
		product *= i
	return product


print(fact(3))
print(fact(5))

fact = counter(fact, c)
print(fact(5))
print(c)

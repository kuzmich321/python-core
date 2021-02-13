import sys
import time
from decimal import Decimal
from math import sqrt

# There are some drawbacks to the Decimal class vs the float class
# - not as easy to code: construction via strings or tuples
# - not all math functions that exist in the math module have a Decimal counterpart
# - more memory overhead
# - performance: much slower than floats (relatively)

a = 3.1415
b = Decimal('3.1415')

print(sys.getsizeof(a))
print(sys.getsizeof(b))


# Variable assignment
def run_float(n=1):
	for i in range(n):
		a = 3.1415


def run_decimal(n=1):
	for i in range(n):
		a = Decimal('3.1415')


n = 1000000
start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)

print('----------------------------')


# Arithmetic operations
def run_float(n=1):
	a = 3.1415
	for i in range(n):
		a + a


def run_decimal(n=1):
	a = Decimal('3.1415')
	for i in range(n):
		a + a


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)

print('----------------------------')


def run_float(n=1):
	a = 3.1415
	for i in range(n):
		sqrt(a)


def run_decimal(n=1):
	a = Decimal('3.1415')
	for i in range(n):
		a.sqrt()


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)
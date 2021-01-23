import math

# Integers support all the standard arithmetic operations + - * / **
# But what is the resulting type of each operation ?
# int + int --> int
# int - int --> int
# int * int --> int
# int ** int --> int
# int / int --> float (obviously 3/4 = 0.75)
# But, also 10 / 2 = 5 (float)

# Two more operators in integer arithmetic
# First, we revisit long integer division...
# 155 / 4 ---> 4 * 38 + 3 ---> 4 * (155 // 4) + (155 % 4)
# // - floor division
# % - modulo operator
# and they always satisfy: n = d * (n // d) + (n % d)

# What is floor division exactly ?
# First define the floor of a (real) number
# The floor of a real number a is the largest (in the standard number order) integer <= a

# floor (3.14) = 3
# floor (2) = 2

# But watch out for negative numbers
print(math.floor(-3.1))

print(135 / 4)

# Negative numbers
# Be careful, a // b, is not the integer portion of a / b, it is the FLOOR(a / b)

print(135 // 4)
print(-135 // 4)

# And, in fact: a = b * (a // b) + a % b
# 4 * (-135 // 4) + (-135 % 4) = (4 * -34) + 1 = -136 + 1 = -135

print('------')

print(type(1 + 1))
print(type(2 * 3))
print(type(2 - 3))
print(type(2 ** 3))
print(type(2 / 3))
print(type(10 / 2))

print('------')

# this is about limiting precision with point numbers
print(math.floor(-3.000000000000001))
print(math.floor(-3.0000000000000001))

print('------')


def my_func(a, b):
	print(f"Simple Division : {a / b}")
	print(f"Native Floor Division : {a // b}")
	print(f"Math Floor Division : {math.floor(a / b)}")
	print(f"Math Truncation : {math.trunc(a / b)}")
	print(f"Mod : {a % b}")
	print('------')


my_func(33, 16)
my_func(-33, 16)
my_func(33, -16)
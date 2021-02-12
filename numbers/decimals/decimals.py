import decimal
from decimal import Decimal

# PEP 327
# Decimal is an alternative to using the (binary) float type. It avoids the approximation issues with floats
# Finite number of significant digits -> rational number

# So why not just use the Fraction class?
# To add two fractions -> common denominator -> complex, requires extra memory

# Why do even care? Why not just use binary floats?
# finance, banking, and any other field where exact finite representations are highly desirable
# let's say we are adding up all the financial transactions that took place over a certain time period
# amount = $100.01      1.000.000.000 transactions
# 100.01 --> 100.01000...051159
# sum    --> $100010000000.00 (exact decimal)
# sum    --> $100009998761.146... (approximate binary float) ... $1238.85... off!!!

# Decimals have a context that controls certain aspects of working with decimals
# <precision> - during arithmetic operations
# <rounding> - algorithm
# This context can be <global> - the default context
# or temporary <local> - sets temporary settings without affecting the global settings

# Working with Global and Local Contexts
x = Decimal('1.25')
y = Decimal('1.35')

# global
global_ctx = decimal.getcontext()  # context (global in this case)
print(global_ctx.prec)  # get or set the precision (value is an int)
print(global_ctx.rounding)  # get or set the rounding mechanism (value is a string)

# local
with decimal.localcontext() as ctx:
	ctx.prec = 2
	ctx.rounding = decimal.ROUND_HALF_UP
	print(ctx)
	print(ctx is decimal.getcontext())
	print(round(x, 1))
	print(round(y, 1))
	# decimal operations performed here will use the ctx context

print(round(x, 1))
print(round(y, 1))
print(global_ctx)

import math

# PEP 485

# To test for <equality> of two floats, you could do the following methods:
# round both sides of the equality expression to the number of significant digits
# print(round(a, 5) == round(b, 5))
# or, more generally, use an appropriate range (R) within which two numbers are deemed equal
# for some R > 0, a=b if and only if |a-b| < R
# i.e are two numbers within x% of each other?
# But there are non trivial issues with using these seemingly simple tests


def is_equal(x, y, eps):
	return math.fabs(x-y) < eps


# Using absolute tolerances...
x = 0.1 + 0.1 + 0.1
y = 0.3
print(format(x, '.20f'), format(y, '.20f'))  # delta = 17th digit after decimal

a = 10000.1 + 10000.1 + 10000.1
b = 30000.3
print(format(a, '.20f'), format(b, '.20f'))  # delta = 12th digit after decimal

abs_tol = 1e-15
print(is_equal(x, y, abs_tol), is_equal(a, b, abs_tol))

# Maybe we should use relative tolerances...
# Using a relative tolerance: rel_tol = 0.001% = 0.00001 = 1e-5
# i.e. maximum allowed difference between the two numbers, <relative> to the larger magnitude of the two numbers
# tol = rel_tol * max(|x|, |y|)
# Using a relative tolerance technique doesn't work well for numbers <CLOSE TO ZERO>!
# tol = max(rel_tol * max(|x|, |y|), abs_tol)

x = 1000.0000001
y = 1000.0000002

a = 0.0000001
b = 0.0000002

print(math.isclose(x, y), math.isclose(a, b))
print(math.isclose(a, b, abs_tol=1e-5))

x = 1000.01
y = 1000.02

a = 0.01
b = 0.02

print(math.isclose(x, y, rel_tol=1e-5, abs_tol=1e-5), math.isclose(a, b, rel_tol=1e-5, abs_tol=1e-5))

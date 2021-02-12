from math import trunc, floor, ceil, copysign

# Float -> Integer ... data loss
# different ways to configure data loss
# 10.4 ... 10? 11?
# 10.5 ... 10? 11?
# 10.6 ... 11
# 10.0001, 10.9999...
# truncation, floor, ceiling, rounding  <-- data loss in all cases
# Truncation - truncating a float simply returns the int portion of the number i.e. ignores everything after
# the decimal point

# The int Constructor will accept a float and it uses truncation when casting the float to an int

# Floor - the floor of a number is the largest integer less than (or equal to) the number
# For positive numbers, floor and truncation are equivalent
# a // b == floor (a / b)
# Ceiling - is kinda opposite of floor

# round(x, n=0) - This will round the number x to the closest multiple of 1e-n
# You might think if this as rounding to a certain number if digits after the decimal point
# which would work for positive n, but n can, in fact, also be NEGATIVE!

# In addition to truncate, floor, and ceiling, we can therefore also use rounding (with n=0) to coerce a float to an int
# If there is no N, then it defaults to zero and round(x) will therefore return an int
# round(x)      --> int
# round(x, n)   --> same type as x
# round(x, 0)   --> same type as x
# BUT !!! Ties... Ex: round(1.25, 1)... there is no closest value!
# We probably would expect round(1.25, 1) to be 1.3
# Similarly, we would expect round(-1.25, 1) to be -1.3
# This type of rounding is called <rounding to nearest, with ties away from zero>

# Banker's Rounding
# IEEE 754 standard:
# rounds to the nearest value, with ties rounded to the nearest value with an even least significant digit
# Why Banker's Rounding? - Less biased(предвзятое) rounding than ties away from zero
# Consider averaging 3 numbers, and averaging the rounded value of each:
# 0.5, 1.5, 2.5                --> avg = 4.5/3 = 1.5
# "standard" rounding: 1, 2, 3 --> avg = 6/3 = 2
# banker's rounding: 0, 2, 2   --> avg = 4/3 = 1/3...

# If you really insist on rounding away from zero...
# One common (and partially incorrect) way to round to nearest unit that often comes up on the web is: int(x + 0.5)
# but, this does not work NEGATIVE numbers
# The correct way to do it:
# sign(x) * int(abs(x) + 0.5)
# sign = 1 if x >= 0 else -
# or we can use math.copysign() to achieve our goal

x = -10.4
y = 10.4

print(int(y) is trunc(y) is round(y))
print(int(x), int(y))
print(floor(x), floor(y))
print(ceil(x), ceil(y))

a = 1.23
b = 18.2
print(round(a), round(a, 1))
print(round(b, -1))

# Banker's Rounding
print(round(1.25, 1))  # towards 0      --> 1.2 (even) < 1.25 < 1.3 (odd)
print(round(1.35, 1))  # away from 0    --> 1.3 (odd)  < 1.35 < 1.4 (even)
print(round(-1.25, 1))  # towards 0     --> -1.3(odd)  < -1.25 < -1.2 (even)
print(round(15, -1))
print(round(25, -1))


def _round(x):
	return int(x + 0.5 * copysign(1, x))


print(round(1.5), _round(1.5))
print(round(2.5), _round(2.5))
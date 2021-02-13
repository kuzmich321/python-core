from decimal import Decimal
from math import sqrt

# Some arithmetic operators don't work the same as floats or integers
# // and % --> also divmod()
# The // and % operators still satisfy the usual equation: n = d * (n // d) + (n % d)
# But for integers, the // operator performs floor division  --> a // b = floor(a/b)
# For Decimals however, it performs truncated division       --> a // b = trunc(a/b)

# We can use the math module, but Decimal objects will first be cast to floats
# - so we lose the whole precision mechanism that made us use Decimal objects in the first place!
# Usually will want to use the ath functions defined in the Decimal class if they are available

x = 0.01
x_dec = Decimal('0.01')

root_float = sqrt(x)
root_mixed = sqrt(x_dec)
root_dec = x_dec.sqrt()

print(type(root_float), type(root_mixed), type(root_dec))
print(format(root_float, '.27f'))
print(format(root_mixed, '.27f'))
print(root_dec)

print('----------------')

print(format(root_float * root_float, '.27f'))
print(format(root_mixed * root_mixed, '.27f'))
print(root_dec * root_dec)

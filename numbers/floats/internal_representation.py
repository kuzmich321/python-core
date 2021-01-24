from fractions import Fraction

# The float class is Python's default implementation for representing real numbers
# The Python (CPython) float is implemented using the <C double> type which (usually!) implements
# the <IEEE 754 double-precision binary float>, also called <binary64>
# The float uses a fixed number of bytes (8 bytes - 64 bits)
# but Python objects have some overhead too (24 bytes)

# These 64 bits are used as follows:
# sign                  -> 1 bit
# exponent              -> 11 bits -> [-1022, 1023]
# significant digits    -> 52 bits -> 15-17 significant (base-10) digits
# <significant digits>  -> for simplicity, all digits except leading and trailing zeros
# significant digits ex: 1.12345, 1234.5, 12345000000, 0.00012345, 12345e^-50, 1.2345e^10

# Representation: decimal
# Numbers can be represented as base-10 integers and fractions:
# 0.75 = 7/10 + 5/100 = 7*10^-1 + 5 * 10^-2                 2 significant digits
# 0.256 = 2/10 + 5/100 + 6/1000                             3 significant digits
# 123.456 = 1*100 + 2*10 + 3*1 + 4/10 + 5/100 + 6/1000      6 significant digits

# Some numbers cannot be represented using a finite number of terms
# Obviously numbers such as: pi=3.14..., sqrt(2)=1.4...
# But even some rational numbers: 1/3=0.(3)

# Representation: binary
# Numbers in a computer are represented using bits, not decimal digits
# instead of powers of 10, we need to use powers of 2
# (0.11)base2 = (1/2 + 1/4)base10 = (0.5 + 0.25)base10 = (0.75)base10 = (1*2^-1 + 1*2^-2)base10
# Similarly:
# (0.1101)base2 = (1/2 + 1/4 + 0/8 + 1/16)base10 = (0.5 + 0.25 + 0.0625)base10 = (0.8125)base10

# The same problem that occurs when trying to represent 1/3 using a decimal expansion also happens
# when trying to represent certain numbers using a binary expression
# 0.1 = 1/10    Using binary fractions, this number DOESN'T HAVE A FINITE REPRESENTATION
# (0.1)base10 = (0.00011 0011 0011...)base2     it keeps recurring

# So, some numbers that do not have a finite decimal representation,
# do not have a finite binary representation, and some do

# (0.75)base10 = (0.11)base2                finite      -> exact float representation
# (0.8125)base10 = (0.1101)base2            finite      -> exact float representation
# (0.1)base10 = (0 0011 0011 0011)base2     infinite    -> approximate float representation

print(float(10))
print(float(10.4))
print(float('12.5'))

a = Fraction(22/7)
print(float(a))

print(0.1)

print(format(0.1, '.15f'))
print(format(0.1, '.25f'))

print(format(0.125, '.25f'))

a = 0.1 + 0.1 + 0.1
b = 0.3

print(a == b, a is b)

print(format(a, '.25f'))
print(format(b, '.25f'))
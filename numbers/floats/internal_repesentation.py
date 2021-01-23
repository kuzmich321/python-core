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

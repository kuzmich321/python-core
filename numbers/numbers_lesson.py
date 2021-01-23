import sys
import time

# Four BUT 5  main types of numbers

# Integer Numbers(Z)     0, +-1, +-2  --->   int
# Rational Numbers(Q)    p\q          --->  fractions.Fraction
# Real Numbers(R)        0, -1, 0.123 --->  float, decimal.Decimal
# Complex Numbers(C)     a + 4j       --->  complex
# Boolean                0(False), 1(True)

# The int data type
# Ex: 0, 10, -100, 100000, ...
# How large can a Python int become (positive or negative)?
# Integers are represented internally using base-2 (binary) digits, not decimal.

# What's the largest (base 10) integer number that can be represented using 8 bits? 2 ** 8 - 1 = 255
# If we cate about handling negative integers as well, then 1 bit is reserved to represent the sign of the number,
# leaving us with only 7 bits for the number itself out of original 8 bits. 2 ** 7 - 1 = 127
# So, using 8 bits we are able to represent all the integers in the range [-127, 127]
# Since 0 does not require a sign, we can squeeze out an extra number, and we end up with the range [-128, 127]

# If we want to use 16 bits to store (signed) integers, our range would be 2 ** 15. Range: [-32,768 ... 32,767]
# Similarly, if we want to use 32 bits to store (signed) integers, our range would be 2 ** 31. [-2,147,483,648 ...]

# If we had an unsigned integer type, using 32 bits our range would be: [0, 2 ** 32] = [0 ... 4,294,967,296]

# In a 32-bit OS: memory spaces (bytes) are limited by their address number -> 32 bits
# 4,294,967,296 bytes of addressable memory = 4,294,967,296 / 1024kB = 4,194,304kB = 4GB
# when you have 32 gigs RAM. something under 4 gigs

# So, how large an integer can be depends on how many bits are used to store the number.
# Some languages (such as Java, C, ...) provide multiple distinct integer data types that use a fixed number of bits:
# Java examples:
# byte - signed 8-bit numbers   -128, ..., 127
# short - signed 16-bit number  -32,768, ..., 32,767
# int signed 32-bit numbers     -2^31, ..., 2^31 - 1
# long signed 64-bit numbers    -2^61, ..., 2^63 - 1

# Python doesn't work that way
# The int object uses a variable number of bits
# Can use 4 bytes(32 bits), 8 bytes (64 bits), 12 bytes (96 bits), etc. That's completely seamless to us.
# [since ints are actually objects, there is a further fixed overhead per integer]
# Theoretically limited only by the amount of memory available
# Ofc, larger numbers will use more memory
# and standard operators such as +, *, etc. will run slower as numbers get larger

# To create an instance of the int we need at least 24 bytes
# it used 4 bytes (32 bits) to store 1
print(sys.getsizeof(1))

print(sys.getsizeof(2**1000))

print((160 - 24) * 8)


def calc(a):
	for i in range(1000000):
		a * 2


print('------')

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)

print('------')

start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end - start)



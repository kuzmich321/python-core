import fractions

# An integer number is an object - an instance of the int class
# The int class provides multiple constructors
# As well as strings (that can be parsed to a number)

# Number Base
# int("123") ---> (123) with the base of 10
# When used with a string, constructor has an optional second parameter: base 2 <= base <= 36
# If the base is not specified, the default is base 10

# Reverse Process
# built-in functions: bin(), oct(), hex()
# bin(10) -> '0b1010'
# oct(10) -> '0o12'
# hex(10) -> '0xa'
# The prefixes in the strings help document the base of the number: int('0xA', 16) -> 10
# These prefixes are consistent with literal integers using a base prefix (no stings attached): a = 0b1010
# What about other bases? Custom code

number = 232
base = 5

digits = []
while number > 0:
	mod = number % base
	number = number // base
	digits.insert(0, mod)

print(digits)

print(hex(15))

print(int(10.5))
print(int(True))
print(int(False))

a = fractions.Fraction(22, 7)

print(a)

print(float(a))
print(int(a))

print(int('12345'))
print(int('101', base=2))
print(int('FF', base=16))
print(int('ff', base=16))

# print(int('b', base=11)) Value error

print(bin(10))
print(oct(10))
print(hex(10))

a = int('101', base=2)
b = 0b101

print(a is b)


def from_base10(number, base):
	if base < 2:
		raise ValueError('Base b must be >= 2')
	if number < 0:
		raise ValueError('Number must be >= 0')
	if number == 0:
		return [0]
	digits = []
	while number > 0:
		number, mod = divmod(number, base)
		digits.insert(0, mod)
	return digits


def encode(digits, digit_map):
	if max(digits) >= len(digit_map):
		raise ValueError('digit_map is not long enough to encode the digits')
	# encoding = ''
	# for d in digits:
	# 	encoding += digit_map[d]
	# return encoding
	return ''.join([digit_map[d] for d in digits])


def rebase_from10(number, base):
	digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	if base < 2 or base > 36:
		raise ValueError('Invalid base: 2 <= base <= 36')
	sign = -1 if number < 0 else 1
	number *= sign

	digits = from_base10(number, base)
	encoding = encode(digits, digit_map)
	if sign == -1:
		encoding = '-' + encoding
	return encoding


print(from_base10(10, 2))
print(from_base10(255, 16))

print(encode([15, 15], '0123456789ABCDEF'))

print(rebase_from10(314, 2))
print(rebase_from10(-3451, 16))

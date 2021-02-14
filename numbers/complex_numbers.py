# The complex class
# Constructor: complex(x, y) --> x=real part, y=imaginary part
# Literals: x + yJ
# x and y (the real and imaginary parts) are stored as floats

# Arithmetic operators work as expected with complex numbers
# // and % operators are not supported

# Other operations
# == and != are supported
# Comparison operators as <,>,<= and >= are not supported

# Functions in the math module will not work
# Use the cmath module instead !!!

a = complex(1, 2)
b = 1 + 2j
print(a == b)
print(b.real, b.imag, b.conjugate())
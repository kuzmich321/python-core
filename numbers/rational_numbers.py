from fractions import Fraction
import math

# Rational numbers are fractions of integer numbers
# Ex: 1/2, -22/7, 0.45=45/100, 8.3/4=83/40, 8.3/1.4=83/14
# The Fraction Class from fractions module
# Fractions are automatically reduced
# Negative sign, if any, is always attached to the numerator
# Standard arithmetic operators are supported: +, -, *, / and result in Fraction objects as well
# We can get numerator and denominator of Fractions by properties

# Fraction(numerator=0, denominator=1)
# Fraction(other_fraction)
# Fraction(float)
# Fraction(decimal)
# Fraction(string)

print(Fraction(numerator=6, denominator=-10))
print(Fraction('22/7'))

x = Fraction(22, 7)

print(f"numerator = {x.numerator} and denominator = {x.denominator}")

# float objects have finite precision => any float object can be written as a fraction!

print(Fraction(0.75))
print(Fraction(1.375))

# Even though pi and square of 2 are both irrational
# internally represented as floats
# => finite precision real number
# => expressible as a rational number
# BUT it is an approximation
print(Fraction(math.pi))
print(Fraction(math.sqrt(2)))

# !!! Converting a float to a Fractional has an important caveat

# Constraining the denominator
x = Fraction(math.pi)
print(x.limit_denominator(10))
print(x.limit_denominator(100))
print(x.limit_denominator(500))

import decimal
from decimal import Decimal

# Decimal(x) -  x can be a variety of types
# integers  --> Decimal(10) = 10
# strings   --> Decimal('0.1') = 0.1
# tuples    --> Decimal((1, (3, 1, 4, 1, 5), -4)) = -3.1415
# other Decimal object
# floats? yes, but not usually done
# Decimal(0.1) = 0.1000...05551 ... Use strings or tuples instead

# Using the tuple constructor
example = Decimal((1, (3, 1, 4, 1, 5), -4))
print(example)

# Context Precision and the Constructor
# Context precision affects math operations. It doesn't affect the constructor

decimal.getcontext().prec = 2
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a, b, a + b)

types = [10, '0.1', (0, (3, 1, 4, 1, 5), -4), a]
for t in types:
	print(Decimal(t))

# Stay away from floats!!!
print(Decimal(0.1), Decimal(0.1) == Decimal('0.1'))

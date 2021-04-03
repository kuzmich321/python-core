from random import uniform
from math import sqrt

# Tuples are...
# Read-only lists... at lest that's how many introductions to Python will present tuples!
# This isn't wrong, but there's a lot more going on with tuples...
# If you only think of tuples as read-only lists, you're going to miss out on some interesting ideas
# We really need to think of tuples also as data records --> position of value has meaning
# This is why we are going to start looking at tuples before we even cover sequence types

# Tuples vs Lists vs Strings

#           Tuples                              Lists                           Strings
#          containers                         containers                       containers
#        order matters                       order matters                    order matters
# <Heterogeneous>/Homogeneous          Heterogeneous/<Homogeneous>             Homogeneous
#        indexable                             indexable                        indexable
#        iterable                              iterable                         iterable
#        immutable                             mutable                          immutable
#        fixed length                      length can change                  fixed length
#        fixed order                       order can change                   fixed order
#                                          can do in-place sorts
#                                          can do in-place reversals

# Immutability of Tuples
# elements cannot be added or removed
# the order of elements cannot be changed
# works well for representing data structures:
# Point: (10, 20) --> x, y
# Circle: (0, 0, 10) --> x, y, radius
# City: ('London', 'UK', 8_780_000)


a = (10, 20, 30)
b = 10, 20, 30
print(type(a), type(b))

a = 'a', 10, 200, 300, 400
x, y, z, *_ = a

print(a[2:5])
print(x, y, z, _)
print(a[0])


class Point2D:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return f'{self.__class__.__name__}(x={self.x}, y={self.y})'


pt = Point2D(10, 20)
print(pt)

a = Point2D(0, 0), Point2D(10, 20)
a[0].x = 100
print(a)

pt1 = (0, 0)
pt2 = (10, 20)


london = ('London', 'UK', 8_780_000)
new_york = ('New York', 'USA', 8_500_000)
beijing = ('Beijing', 'China', 21_000_000)

cities = [london, new_york, beijing]

total_population = 0
for *_, population in cities:
	total_population += population
print(total_population)

total_population = sum(city[2] for city in cities)
print(total_population)

record = ('DJIA', 2018, 1, 19, 25_987, 26_072, 25_942, 26_072)
symbol, year, month, day, open_, high, low, close = record
symbol, *_, close = record
print(symbol, close)

for index, city in enumerate(cities):
	print(index, city)


def random_shot(radius):
	random_x = uniform(-radius, radius)
	random_y = uniform(-radius, radius)
	is_in_circle = (sqrt(random_x**2 + random_y**2) <= radius and True) or False

	return random_x, random_y, is_in_circle


attempts = 100
count_inside = 0

for i in range(attempts):
	*_, is_in_circle = random_shot(1)
	if is_in_circle:
		count_inside += 1


print(f'Pi is approximately: {4 * count_inside / attempts}')

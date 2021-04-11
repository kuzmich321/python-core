from collections import namedtuple
from random import randint, random


def random_color():
	red = randint(0, 255)
	blue = randint(0, 255)
	green = randint(0, 255)
	alpha = round(random(), 2)
	return red, green, blue, alpha


color = random_color()
red, green, blue, alpha = color
print(red, green, blue, alpha)

Color = namedtuple('Color', 'red green blue alpha')


def random_color():
	red = randint(0, 255)
	blue = randint(0, 255)
	green = randint(0, 255)
	alpha = round(random(), 2)
	return Color(red, green, blue, alpha)


color = random_color()
print(color)

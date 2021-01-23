# Underscore before an attr or a method means that this is private
class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width

    def set_width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError('Width must be positive.')

    # This gets printed when calling str(an instance)
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)

    # This gets printed when calling just an instance
    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._width, self._height)

    # When we need to compare the objects are the same
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self._width == other._width and self._height == other._height
        else:
            return False

    # Less than
    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

    def area(self):
        return self._width * self._height

    def perimeter(self):
        return (self._width + self._height) * 2


class Rectangle2:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError('Width must be positive.')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        else:
            self._height = height

    # Those are not having _ before them
    def __str__(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)


r1 = Rectangle(10, 20)
r2 = Rectangle(100, 20)

# There are different objects
print(r1 is not r2)

# __eq__ method works
print(r1 == r2)

# We defined __lt__ method. It checked __gt__ is not settled and just switched it
print(r2 > r1)

r1.set_width(100)
print(r1.get_width())

r3 = Rectangle2(10, 20)
# r3.width = -20
print(r3)

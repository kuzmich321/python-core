from collections import namedtuple

# Named Tuples are Immutable
# So how can we "change" one or more values inside the tuple?
# Just like with strings, we have to create a new tuple, with the modified values

Point2D = namedtuple('Point2D', 'x y')
pt = Point2D(0, 0)
pt = Point2D(100, pt.y)
print(pt)

# Maybe slicing or unpacking?
Stock = namedtuple('Stock', 'symbol year month day open high low close')
stock = Stock('DJIA', 2021, 1, 25, 26_313, 26_322, 26_410, 26_393)
current = stock[:7]
*current, _ = stock
stock = Stock(*current, 26_555)
print(stock)

# We can also use the <_make> class method - but we need to create an iterable that
# contains all the values first
current = stock[:7]
new_values = current + (26_444,)
stock = Stock._make(new_values)
print(stock)

# This still has drawbacks
# What if we wanted ti change a value in the middle, say day?
pre = stock[:3]
post = stock[4:]
new_values = pre + (26,) + post
stock = Stock(*new_values)
print(stock)

# But event this still has drawbacks!
# How about modifying both the day and the high values?

# The <_replace> instance method
stock = stock._replace(day=27, high=27_000, close=26_777)
print(stock)

# Extending a Named Tuple
# Sometimes we want to create named tuple that extends another named tuple, appending one or more fields
Stock = namedtuple('Stock', 'symbol year month day open high low close')

# We want to create a new named tuple class, StockExt that adds a single field, prev_close
# When dealing with classes, this is sometimes done by using subclassing.
# But this not easy to do with named tuples
# And there is a cleaner way of doing it anyway

new_fields = Stock._fields + ('prev_close',)
StockExt = namedtuple('StockExt', new_fields)
stock = Stock('DJIA', 2021, 1, 25, 26_313, 26_322, 26_410, 26_393)
stock_ext = StockExt(*stock, 26_000)
print(stock_ext)



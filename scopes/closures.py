# Free Variables and Closures
# Remember: Functions defined inside another function can access the outer (nonlocal) variables
def outer():
	x = 'python'

	def inner():
		print(f'{x} rocks!')  # <-- this nonlocal variable x is called a <free> variable

	inner()


outer()


# This is called a <closure>
# x = 'python'
#
# 	def inner():
# 		print(f'{x} rocks!')

# Returning the inner function
def outer():
	x = 'python'

	def inner():
		print(f'{x} rocks!')

	return inner  # when we return inner, we are actually "returning" the closure


# when we called fn AT THAT TIME Python determined the value of x if tne extended scope
# But notice that outer has finished running BEFORE we called fn - it's scope was "gone"
fn = outer()
fn()


# Python Cells and Multi-Scoped Variables
# Here the value of x is <shared> between two scopes
# The label x is in two different scopes but always reference the same "value"
#  Python doest it by creating a <cell> as an intermediary object
# outer.x AND inner.x --> Cell --> x (string='python')
# In effect, both variables x (in outer and inner), point to the same cell
# When requesting the value of the variable, Python will "double-hop" to get to the final value
# That's why it works. When outer is gone inner.x is still pointing to Cell
def outer():
	x = 'python'

	def inner():
		print(x)
	return inner


# Closures
# You can think if the closure as a function + an extended scope that contains the free variables
# The free variable's value is the object the cell points to - so that could change over time!
# Every time the function in the closure is called and the free variable is referenced:
# Python looks up the <cell> object, and then whatever the cell is pointing to
def outer():
	a = 100

	# Closure #
	x = 'python'
	print(hex(id(x)))
	def inner():
		a = 100
		print(hex(id(x)))
		print(f'{x} rocks!')
	# Closure #
	return inner


fn = outer()  # fn = inner + extended scope. x is pointing to the cell
print(fn.__code__.co_freevars)
print(fn.__closure__)
outer()
fn()
print('---------------')


# Modifying free variables
def counter():
	count = 0

	def inc():
		nonlocal count
		count += 1
		return count
	return inc


fn = counter()
print(fn())
print(fn())
print(fn())
print('---------------')


# Multiple Instances of Closures
# Every time we run a function, a <new> scope is created
# If that function generates a closure, a new closure is created every time as well
# They are different instances of the closure
# The cells are different
f1 = counter()
f2 = counter()
print(f1())
print(f1())
print(f2())
print('---------------')


# Shared Extended Scopes
def outer():
	count = 0

	def inc1():
		nonlocal count
		count += 1
		return count

	def inc2():
		nonlocal count
		count += 1
		return count

	return inc1, inc2


f1, f2 = outer()
print(f1())
print(f2())
print('---------------')


# You may think this shared extended scope is highly unusual... but it's not!
def adder(n):
	def inner(x):
		return x + n
	return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

print(add_1(10))
print(add_2(10))
print(add_3(10))
print('---------------')

# But suppose we tried doing it this way:
adders = [lambda x: x + n for n in range(1, 4)]
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
print(adders[0].__closure__)
print('---------------')


def create_adders():
	return [lambda x: x + n for n in range(1, 4)]


adders = create_adders()
print(adders[0].__closure__)
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
print('---------------')


def create_adders():
	return [lambda x, y=n: x + y for n in range(1, 4)]


adders = create_adders()
print(adders[0](10))
print(adders[1](10))
print(adders[2](10))
print('---------------')


# Nested Closures
def increment(n):
	# inner + n is a closure
	def inner(start):
		current = start

		# inc + current + n is a closure
		def inc():
			nonlocal current
			current += n
			return current
		return inc
	return inner


fn = increment(2)
print(fn.__code__.co_freevars)
inc_2 = fn(100)
print(inc_2.__code__.co_freevars)
print(inc_2())
print(inc_2())


print('---------------')


def outer():
	x = [1, 2, 3]
	print(hex(id(x)))

	def inner():
		print(hex(id(x)))
	return inner


fn = outer()
fn()

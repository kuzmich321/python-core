# Inner Functions
# We can define functions from inside another function
# Both functions have access to the global and built-in scopes as well as their respective local scopes
# But the inner function also has access to its enclosing scope - the scope of the outer function
# That scope is neither local nor global - it is called <nonlocal> scope
def outer_func():
	def inner_func():
		pass
	inner_func()


outer_func()


# Referencing variables from the enclosing scope
# When we cann outer_func, inner_func is created and called
# When inner_func is called, Python does not find a in the local (inner_func) scope
# So it looks for it in the enclosing scope, in this case the scope of outer_func
def outer_func():
	a = 10

	def inner_func():
		print(a)

	inner_func()


outer_func()

# Since it does not find it there either, it looks in the enclosing (global) scope
a = 10
def outer_func():
	def inner_func():
		print(a)

	inner_func()


outer_func()


# Modifying global variables
def outer_func():
	def inner_func():
		global a
		a = 'hello'

	inner_func()


outer_func()
print(a)


# Modifying nonlocal variables
# When inner_func is compiled, Python sees an assignment to x
# So it determines that x is a local variable to inner_func
# The variable x in inner_func <masks> the variable in outer_func
# Just as with global variables, we have to <explicitly> tell Python we are modifying a nonlocal variable
def outer_func():
	x = 'hello'

	def inner_func():
		x = 'python'

	inner_func()
	print(x)


outer_func()


# Beware: It will look in local scopes, it will NOT look in the global scope
def outer_func():
	x = 'hello'

	def inner_func():
		nonlocal x
		x = 'python'

	inner_func()
	print(x)


outer_func()
print('----------------------')


# But consider this example
def outer_func():
	x = 'hello'

	def inner1():
		x = 'python'

		def inner2():
			nonlocal x
			x = 'ninja'
		print('inner(before):', x)
		inner2()
		print('inner(after):', x)

	inner1()
	print('outer:', x)


outer_func()
print('----------------------')


# And this
def outer_func():
	x = 'hello'

	def inner1():
		nonlocal x
		x = 'python'

		def inner2():
			nonlocal x
			x = 'ninja'
		print('inner(before):', x)
		inner2()
		print('inner(after):', x)

	inner1()
	print('outer:', x)


outer_func()
print('----------------------')


# Nonlocal and Global Variables
x = 100


def outer_func():
	x = 'python'

	def inner1():
		nonlocal x
		x = 'ninja'

		def inner2():
			global x
			x = 'hello'
		print('inner(before):', x)
		inner2()
		print('inner(after):', x)

	inner1()
	print('outer:', x)


outer_func()
print(x)

# Scopes and Namespaces
# When an object points to some object and we say that the variable (name) is <bound> to that object
# That object can be accessed using that name in various parts of our code
# But not just anywhere!
# That variable name is it's binding (name and object) only "exist" is specific parts of out code
# the portion of code where that name/binding is defined, is called the <lexical scope> of the variable
# these bindings are stored in namespaces

# The Global Scope
# The global scope is essentially the <module> scope
# It spans a single file only
# There is no concept of a truly global (across all the modules in out entire app) scope in Python
# The only exception to this are some of the built-in globally available objects, such as: True, False, None, print...
# The built-on and global variables can be used anywhere inside our module
# Global scopes are nested inside the built-in scope

# The Local Scope
# When we create functions, we can create variable names inside those functions (using assignments)
# Variables defined inside a function are not created until the function is <called>
# Every time the function is called, <a new scope is created>
# Variables defined inside the function are assigned to that scope
# The actual object the variable references could be <different> each time the function is called
# (this is why recursion works!)
# When the function finishes running, the scope is gone too!

# Nested Scopes
# Scopes are often nested
# Built-in Scope --> Module Scope --> Local Scope

# Namespace lookups
# When requesting the object bound to a variable name: e.g print(a)
# Python will try to find the object bound to the variable
# - in current local scope first
# - works up the chain of enclosing scope

# Accessing the global scope from a local scope
# When retrieving the value of a global variable from inside a function, Python automatically searches
# the local scope's namespace, and up the chain of all enclosing scope namespaces

# The global keyword
# We can tell Python that a variable is meant to scoped in the global scope by using the <global> keyword

# Global and Local Scoping
# When Python encounters a function definition at <compile-time>
# It will <scan> for any labels (variables) that have values assigned to them (anywhere in the function)
# if the global has not been specified as global, then it will be local
# Variables that are referenced but <not assigned> a value anywhere in the function will <not be local>,
# and Python will, at <run-time>, look for them in enclosing scopes

a = 10


def my_func(n):
	c = n ** 2
	return c


def my_func2(n):
	print('global a:', a)
	c = a ** n
	return c


def my_func3(n):
	a = 20
	c = a ** n
	return c


def my_func4(n):
	global a
	a = 20
	c = a ** n
	return c


def my_func5():
	global var
	var = 'hello world'
	return


def my_func6():
	try:
		print('global a:', a)
		a = 'hello'
	except UnboundLocalError:
		a = 'hello'
		print('local a:', a)

print(my_func2(2))
print(my_func3(2))
print(my_func4(2))
print(my_func2(2))
my_func5()
print(var)
my_func6()

f = lambda n: print(a**n)
f(2)
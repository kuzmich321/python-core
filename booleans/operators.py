# Boolean Operators and Truth Values
# Normally, Boolean operators are defined to operate on and return Boolean values
# But every object in Python has a truth value (truthiness)
# so, for any object X and Y, we could also write bool(X) and bool(Y)
# in fact, we don't need to use bool()  --> X and Y, X or Y
# So what is returned when evaluating these expressions?
# A Boolean? No!

# Definition of <or> in Python
# X or Y: if X is truthy, returns X, otherwise returns Y
# Does this work as expected when X and Y are Boolean values?
# If X is truthy, returns X, otherwise evaluates Y and returns it

# Definition of <and> in Python
# X and Y: if X is falsy, returns X, otherwise returns Y
# If X is falsy, returns X, otherwise evaluates Y and returns it

# Consequence: or
# Ex:
# a = s1 or s2 or s3 or 'N/A'
# In this case, a will be equal to the first truthy value (left to right evaluation)
# and is guaranteed to have a value, since 'N/A' is truthy
# Ex: We have an int value that cannot be zero
# a = a or 1

# Consequence: and
# Ex:
# x=10, y=20/x
# x=0, y=20/x
# Seems like we are able to avoid a division by zero error using the <and> operator
# x = a and total/a
# Ex: Computing an average
# avg = n and sum/n
# Ex: You want to return the first char of a string or an empty string if the string is None or empty
# return (s and s[0]) or ''

# The Boolean <not>
# not is a built-in function that returns a Boolean value

# X or Y
print('' or [1, 2])
print(1 or 1/0)

s1 = None
s2 = ''
s3 = 'abc'

s1 = s1 or 'n/a'
s2 = s2 or 'n/a'
s3 = s3 or 'n/a'

print(s1, s2, s3)

print([] or [0])
print(None or [0])

print('---------------------')

# X and Y
print(None and 100)
print([] and [0])

a = 2
b = 4

# The same as b and a/b
if b == 0:
	print(0)
else:
	print(a/b)

print(b and a/b)

s1 = None
s2 = ''
s3 = 'abc'

s1 = (s1 and s1[0]) or 'nothing'
s2 = (s2 and s2[0]) or 'nothing'
s3 = (s2 and s3[0]) or 'nothing'

print(s1, s2, s3)

print('---------------------')

# The not operator
print(not True)
print(not False)

print(not bool('abc'))
print(not bool(''))

print(not 'abc')
print(not '')

print(type(not 'abc'))

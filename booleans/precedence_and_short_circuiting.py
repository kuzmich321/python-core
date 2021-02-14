import string

# The Boolean Operators: not, and, or
# Operator Precedence
# ()
# < > <= >= == != in is
# not
# and
# or

# Ex: True or True and False == True or (True and False) --> True of False --> True
# But: (True or True) and False --> True and False --> False

# When in doubt, or to be absolutely sure, use parentheses!
# Also, use parentheses to make your code more <human readable>!
# a < b or a > c and not x or y == (a < b) or ((a > c) and (not x)) or y

# Short-Circuit Evaluation
# if X is True, then X or Y will be True no matter the value of Y
# So, X or Y will return True without evaluating Y if X is True
# If X if False, then X and Y will be False no matter the value of Y

# Ex:
# Scenario: There is some data feed that lists a stock symbol, and some financial data.
# Your job is to monitor this feed, looking for specific stock symbols defined in some watch list, and react only if
# the current stock price is above some threshold. Getting the current stock price has an associated cost

# If Boolean expressions did not implement short-circuiting, you would probably write:
# if symbol in watch_list:
#   if price(symbol) > threshold
# But because of short-circuit evaluation you could write this equivalently as:
# if symbol in watch_list abd price(symbol) > threshold:

# Ex:
# name is a string returned from a nullable text field in a database
# perform some action if the first char of name is a digit (0-9)
# if name[0] in string.digits --> this code will break if name is None or an empty string, so
# if name and name[0] in string.digits

print(True or True and False)
print((True or True) and False)

a = 10
b = 0
if b and a/b > 2:
	print('a is at least twice 2')

name = '1me'
if name and name[0] in string.digits:
	print("Name cannot start with a digit")

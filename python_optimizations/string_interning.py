import sys
import time

# https://stackabuse.com/guide-to-string-interning-in-python/

# Some strings are also automatically interned - but not all!

# As the Python is compiled, identifiers are interned
# Variable names
# Function names
# Class names
# etc

# Identifiers
# must start with _ or a letter
# can only contain _, letters and numbers

# Some strings literals may also be automatically interned:
# sting literals that look like identifiers (e.g. 'hello world')
# although it it starts with a digit, even though that is not a valid identifier, it may still get interned
# BUT DON'T COUNT ON IT

# Why do this?
# It's all about (speed and, possibly, memory) optimization
# Python, both, internally, and in the code you write, deals with lots and lots of dictionary type lookups,
# on string keys, which means a lot of string equality testing

# Ex: print(a). Python will check it in its internal dictionary

# Let's say we want to see if two string are equal:

a = 'some_long_string'
b = 'some_long_string'

# because it looks like identifier
print(a is b)

# Using a == b, we need to compare the two strings character by character
# But if we know that 'some_long_string' has been interned, then a and b are the same thing if they both point
# to the same memory address

# In which case we can use a is b instead - which compares two integers (memory address)
# This is much faster than the char by char comparison

# Not all strings are automatically interned by Python
# But you can force strings to be interned by using the sys.intern() method
# (Basically making that particular string to be a Singleton)

a = sys.intern('the1quick1brown1fox asd asd asd asd')
b = sys.intern('the1quick1brown1fox asd asd asd asd')
print(a is b)

# When should you do it?
# dealing with a large number of strings that could have high repetition e.g. tokenizing a large corpus of text (NLP)
# lots of string comparisons

s1 = 'hello world'
s2 = 'hello world'

print(s1 is s2)


def compare_using_equals(n):
    s3 = 'a long string that is not interned' * 200
    s4 = 'a long string that is not interned' * 200
    for i in range(n):
        if s3 == s4:
            pass


def compare_using_interning(n):
    s3 = 'a long string that is not interned' * 200
    s4 = 'a long string that is not interned' * 200
    for i in range(n):
        if s3 is s4:
            pass


start = time.perf_counter()

compare_using_equals(10000000)

end = time.perf_counter()
print(end - start)

print('---------')

start = time.perf_counter()

compare_using_interning(10000000)

end = time.perf_counter()
print(end - start)
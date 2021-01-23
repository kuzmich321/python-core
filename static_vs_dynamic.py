# Some languages (Java, C++, Swift) are statically typed
# String myVar = 'hello';
# You can't do like that later on: myVar = 10; It's another data type
# What you could do: myVar = 'abc';

# Python is dynamically typed

# The variable my_var is purely a reference to a string object with value hello
# No type is "attached" to my_var
my_var = 'hello'
# The variable my_var is now pointing to an integer object with value 10
my_var = 10

# We might think the type of my_var has changed. Well my_var never had a type
# to start off with. my_var was just a reference. What has changed
# is the type of the object that my_var was pointing to

# We can use type() to determine the type of the object currently referenced by a variable
print(type(my_var))

a = 'hello'
a = 10
a = lambda x: x**2
a = 3 + 4j

print(type(a))
# Code Organization, Ease of Use...
# Suppose you have 50 different functions and classes in your program
# Start with Modules...
"""
api/
	api.py
	dbutilities.py
	jsonutilities.py
	typeconversions.py
	validations.py
	authentication.py
	authorization.py
	users.py
	blogposts.py
	logging.py
	unittests.py

	but still - everything at the top level
	too many imports
	...
	certain utilities could be broken down further:
	dbutilities ==> connections, queries
	users ==> User, Users, UserProfile

	certain modules belong "together"
	authorization, authentication ==> security
"""

"""
api/
	utilities/
		__init__.py
		database/
			__init__.py
			connections.py
			queries.py
		json/
			__init__.py
			encoders.py
			decoders.py
	security/
		__init__.py
		authorization.py
		authentication.py
	models/
		__init__.py
		users/
			__init__.py
			user.py
			userprofile.py
"""

# Another User Case
# You have a module that implements 2 functions/classes for users of the module
# Those two objects require 20 different helper functions and 2 additional helper classes
# From module developer's perspective:
# it's much easier to break the code down into multiple modules
# From module user's perspective:
# they just want a single import for the function and the class
# (i.e, it should look like a single module)

# Module Developer's Perspective
"""
mylib/
	__init__.py
	submod1.py ==> func to be exported to user lives here
	submod2.py
	subpack1/
		__init__.py
		pack1mod1.py
		pack1mod2.py ==> class to be exported to user lives here
"""

# Module User's Perspective
# User should not have to write:
# from mylib.submod1 import my_func
# from mylib.subpack1.pack1mod2 import MyClass

# Much easier for user if ther could write:
# from mylib import my_func, MyClass
# or simply:
# import mylib

# Using __init__.py
# We can use packages' __init__.py code to export (expose) just what's needed by our users
# In the example above we can write to mylib.__init__.py the following:
"""
from mylib.submod1 import my_func
from mylib.subpack1.pack1mod2 import MyClass
"""

# So, why Packages?
# ability yo break code up into smaller chunks, makes out code:
"""
easier to write
easier to test and debug
easier to read/understand
easier to document
"""
# but they can still be "stitched" together
# hides inner implementation from user

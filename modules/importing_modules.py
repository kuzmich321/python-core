import sys

# The first thing to note is that Python is doing the import at <run time>, i.e while your code is actually running
# This is different from traditional compiled languages such as C where module are compiled and linked at compile time
# In both cases through, the system need to know where those code files exist.
# Python uses a relatively complex system of how to find and load modules
# The sys module has a few properties that define where Python is going to look for modules
# (either built-in or standard library as well as our own or 3rd party)

# Where is Python installed?
print(sys.prefix)

# Where are the compiled C binaries located?
print(sys.exec_prefix)

# Where does python looks for imports?
print(sys.path)

# Basically when we import a module, Python will search for the module in the paths contained in sys.path
# If does not find the module in one of those paths, the import will fail
# So if you ever run into a problem where Python is not able to import a module or package,
# you should check this first to make sure the path to your module/package is in that list

# At high level, this is how Python imports a module from file:
# - checks the sys.modules cache to see of the module has already been imported -
# if so it simply uses the reference in there, otherwise:
# - creates anew module object (types.ModuleType)
# - loads the source code from file
# - adds an entry to sys.modules with name as key and the newly created
# - compiles and executes the source code

# One thing that's really to important to note is that when a module is imported, the module code is <executed>

# Example 1
# This example shows that when we import a module, the module code is actually <executed>.
# Furthermore, that module now has its own namespace that can be seen in __dict__.

# Example 2
# In this example, we can see that when we import a module, Python first looks for it in sys.modules

# Example 3a
# In this example we look at a simplified view of how Python imports a module
# We use two built-in functions, <compile> and <exec>
# The compile function compiles source (e.g text) into a code object
# The exec function is used to execute a code object. Optionally we can specify what dictionary should be used
# to store global symbols

# Example 3b
# This is essentially the same as example 3a, except we make our importer into a function
# and use it to show how we technically should look for a cached version of the module first

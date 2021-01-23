# Important Note:
# A lot of we discuss with memory management, garbage collection and optimizations
# is usually specific to thy Python implementation you use.

# In this course, we're using CPython, the standard (or reference) Python implementation (written in C)

# But there are other Python implementations out there. These include:
# - JPython - written in Java and can import and use any Java class - in fact it even compiles to Java bytecode
# which can then run in JVM (Java Virtual Machine)
# - IronPython - This one is written in C# and targets .Net (and mono) CLR
# - PyPy - This one is written in RPython (which is itself a statically-typed subset of Python
# written in C that is specifically designed to write interpreters)
#   and many more...

# Interning: reusing objects on-demand
# At startup, Python (Cpython), pre-loads (caches) a global list of integers in the range [-5, 256]
# Any time an integer is referenced in that range, Python will use the cached version of that object
# Integer in that range is the Singleton

a = 10
b = 10

print(a is b)

a = 1000000
b = 1000000
print(a is b)

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)

print(a is b is c is d)

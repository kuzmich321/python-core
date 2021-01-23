import sys
import ctypes


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


# This is a convention to indicate private objects
# Objects named this way won't get imported by a statement such as: from module import *
_my_var = 123

# Used to "mangle" class attributes-useful in inheritance chains
__my_var = 123

# User for system-defined names that have a special meaning to the interpreter
# Don't invent them, stick to the ones pre-defined by Python!
# Example: x < y ---> x.__lt__(y)
__my_var__ = 123

# Packages. Short, all-lowercase names. Preferably no underscores ---> utilities
# Modules. Short, all-lowercase names. Can have underscores ---> db_utils, dbutils
# Classes ---> BankAccount
# Functions (snake_case) ---> open_account
# Variables (snake_case) ---> account_id
# Constants. all-uppercase, words separated by underscores ---> MIN_APR


# In Python everything is an Object
# Every variable references a slot in memory


# REFERENCE COUNTING
other_var = _my_var
# When counter is 0 (there are no references left) then Python throws away the object
a = [1, 2, 3]

# It becomes two because of getrefcount function creates another one
print(sys.getrefcount(a))

# This doesn't create an extra count
print(ref_count(id(a)))

b = a
c = 10
print(ref_count(id(a)))

a_id = id(a)
a = None
print(ref_count(a_id))


# VARIABLE RE-ASSIGNMENT
# We're not changing the value. We are creating a new object
my_var = 10
my_var = 15

# The same thing happens
# In fact, the value inside the int objects, can never be changed
my_var = my_var + 5

# Both are pointing to the same memory slot
num_1 = 10
num_2 = 10

print(hex(id(num_1)), hex(id(num_2)))

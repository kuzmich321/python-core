# GARBAGE COLLECTION
# Sometimes Reference Counting mistakes in particular it's called Circular Reference
# Ex: my_var points to Obj A. Obj A points to Obj B (my_var2)
# If we remove my_var then Reference Counting is not able to destroy the objects
# It's a Memory Leak
# That's where Garbage Collector comes in and it's gonna clean it up

# Garbage Collector
# - Can be controlled programmatically using gc module
# - By default it's turned on
# - You may turn it off if you're sure your code doesn't create circular references - but beware!!!
# - Runs periodically on its own (if turned on)
# - You can call it manually, and even do your own cleanup

# In general GC works just fine but, not always...
# for Python < 3.4 ...

import ctypes
import gc


def ref_count(address: int):
    return ctypes.c_long.from_address(address).value


def obj_by_id(object_id):
    for obj in gc.get_objects():
        if id(obj) == object_id:
            return "Object exists"
    return "Not Found"


class A:
    def __init__(self):
        self.b = B(self)
        print("A: self: {0}, a: {1}".format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        print("B: self: {0}, a: {1}".format(hex(id(self)), hex(id(self.a))))


gc.disable()

my_var = A()

print(hex(id(my_var.b)))
print(hex(id(my_var.b.a)))

a_id = id(my_var)
b_id = id(my_var.b)

print(ref_count(b_id), ref_count(a_id))

my_var = None

print(ref_count(b_id), ref_count(a_id))

print(obj_by_id(a_id), obj_by_id(b_id))

gc.collect()

print(obj_by_id(a_id), obj_by_id(b_id))
print(ref_count(a_id), ref_count(b_id))
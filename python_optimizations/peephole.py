import string
import time

# This is another variety of optimizations that can occur at compile time.

# Constant expressions
# numeric calculations like 24 * 60
# Python will actually pre-compile 24 * 60 -> 1440
# Short sequences length < 20 like (1, 2) * 3 -> (1, 2, 1, 2, 1, 2)
# 'abc' * 3 -> abcabcabc
# 'hello' + 'world' -> hello world
# BUT NOT 'the quick brown fox' * 10 (more than 20 characters)

# Membership Tests: Mutables are replaced by Immutables
# if e in [1, 2, 3]:
# are encountered, the [1, 2, 3] constant, is replaced by its immutable counterpart like tuple (1, 2, 3)
# lists -> tuples
# sets -> frozen sets

# Set Membership is much faster than list or tuple membership (sets are basically like dictionaries)
# So, instead of writing if e in [1, 2, 3]: or if e in (1, 2, 3):
# write if e in {1, 2, 3}:

def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a', 'b'] * 3   # this is not constant because it's Mutable


print(my_func.__code__.co_consts)


def my_func(e):
    if e in [1, 2, 3]:
        pass


print(my_func.__code__.co_consts)


def my_func(e):
    if e in {1, 2, 3}:
        pass


print(my_func.__code__.co_consts)

print('---------')

print(string.ascii_letters)

char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

print(char_list)
print(char_tuple)
print(char_set)


def membership_test(n, container):
    for i in range(n):
        if 'z' in container:
            pass


start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list: ', end - start)

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple: ', end - start)

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('set: ', end - start)
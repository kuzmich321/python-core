from functools import lru_cache
from time import perf_counter

def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)


class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}


    def fib(self, n):
        if n not in self.cache:
            print(f'Calculating fib({n})')
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        else:
            print('Taking from cache...')
        return self.cache[n]


# f = Fib()
# f.fib(10)
# f.fib(10)


def fib():
    cache = {1: 1, 2: 1}

    def calc_fib(n):
        if n not in cache:
            print(f'Calculating fib({n})')
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        else:
            print('Taking from cache...')
        return cache[n]
    return calc_fib


fib()(10)


def memoize(fn):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner


@memoize
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)


fib(10)
fib(11)


@memoize
def fact(n):
    print(f'Calculating {n}!')
    return 1 if n < 2 else n * fact(n-1)


fact(6)
fact(7)


start = perf_counter()
print(fib(200))
end = perf_counter()
print(start - end)


@lru_cache()
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)


fib(10)
fib(11)


@lru_cache(maxsize=8)
def fib(n):
    print(f'Calculating fib({n})')
    return 1 if n < 3 else fib(n-1) + fib(n-2)


fib(8)
fib(9)
fib(9)
fib(1)
fib(3)
fib(2)
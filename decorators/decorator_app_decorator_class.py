def my_dec(a, b):
    def decorator(fn):
        def inner(*args, **kwargs):
            print(f'decorated function called: a={a}, b={b}')
            return fn(*args, **kwargs)
        return inner
    return decorator


@my_dec(10, 20)
def my_func(s):
    print(f'Hello {s}')


my_func('World')


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, c):
        print(f'called a={self.a}, b={self.b}, c={c}')


obj = MyClass(10, 20)
obj(100)


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, fn):
        def inner(*args, **kwargs):
            print(f'decorated function called: a={self.a}, b={self.b}')
            return fn(*args, **kwargs)
        return inner


@MyClass(15, 25)
def my_func(s):
    print(f'Hello {s}')


my_func('World')

s = [1, 2, 3]


print(len(s))


def func_1():
    print('Running func_1')


def func_2(a: int, b: int):
    return a * b


def func_3():
    return func_4()


def func_4():
    return 'running func_4'


print(func_3())


fn1 = lambda x: x**2


print(fn1(3))
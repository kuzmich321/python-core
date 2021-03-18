# In order for this to work as intended:
# @timed(10)
# def my_func():

# timed(10) will need to return our original timed decorator when called

# Decorator Factories
# The outer function is not itself a decorator
# instead it returns a decorator when called
# We call this outer function a decorator <factory> function
# (It creates a new decorator each time it's called)
def timed(reps):
    def decorator(fn):
        from time import perf_counter

        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                fn(*args, **kwargs)
                total_elapsed += (perf_counter() - start)
            avg_elapsed = total_elapsed / reps
            print(avg_elapsed)
        return inner
    return  decorator



def my_func():
    pass


my_func = timed(10)(my_func)
my_func()


@timed(10)
def my_func():
    pass


my_func()
print('-----------------------')


def dec_factory():
    print('running dec_factory')

    def decorator(fn):
        print('running decorator')

        def inner(*args, **kwargs):
            print('running inner')
            return fn(*args, **kwargs)

        return inner
    return decorator


dec = dec_factory()


@dec
def my_func():
    print('running my_func')


my_func()


@dec_factory()
def my_func():
    print('running my_func')

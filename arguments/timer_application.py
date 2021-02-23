import time


def time_it(fn, *args, rep=1, **kwargs):
	start = time.perf_counter()
	for i in range(rep):
		fn(*args, **kwargs)
	end = time.perf_counter()
	print(f"{fn.__name__} - {(end - start) / rep}")


time_it(print, 1, 2, 3, sep=' - ', end=' ***\n', rep=5)


def compute_powers_1(n, *, start=1, end):
	# using a for loop
	results = []
	for i in range(start, end):
		results.append(n**i)
	return results


print(compute_powers_1(2, end=5))


def compute_powers_2(n, *, start=1, end):
	# using a list comprehension
	return [n**i for i in range(start, end)]


print(compute_powers_2(2, end=5))


def compute_powers_3(n, *, start=1, end):
	# using generator
	return (n**i for i in range(start, end))


def compute_powers_3_v2(n, *, start=1, end):
	return list((n**i for i in range(start, end)))


print(list(compute_powers_3(2, end=5)))

time_it(compute_powers_1, 1, start=0, end=20000, rep=5)
time_it(compute_powers_2, 1, start=0, end=20000, rep=5)
time_it(compute_powers_3, 1, start=0, end=20000, rep=5)
time_it(compute_powers_3_v2, 1, start=0, end=20000, rep=5)

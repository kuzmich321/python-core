from .calculator import Calc

def say_hello(name):
	return f'Hello {name}'


def factorial(n):
	return (n <= 1 and 1) or n * factorial(n-1)

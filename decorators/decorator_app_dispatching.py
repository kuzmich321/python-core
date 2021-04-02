from decimal import Decimal
from html import escape
from numbers import Integral
from collections.abc import Sequence
from functools import singledispatch


def html_escape(arg):
	return escape(str(arg))


def html_int(a):
	return f'{a}(<i>{str(hex(a))}</i>)'


def html_real(a):
	return f'{round(a, 2)}:.2f'


def html_str(s):
	return html_escape(s).replace('\n', '<br/>\n')


def html_list(l):
	items = (f'<li>{html_escape(item)}</li>' for item in l)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


def html_dict(d):
	items = (f'<li>{k}={v}</li>' for k, v in d.items())
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(html_str("""this is
a multi line string
with special chars: 10 < 100
"""))
print(html_int(255))
print('---------------')
print(html_escape(3+10j))


def htmlize(arg):
	registry = {
		object: html_escape,
		int: html_int,
		float: html_real,
		Decimal: html_real,
		str: html_str,
		list: html_list,
		tuple: html_list,
		set: html_list,
		dict: html_dict
	}

	fn = registry.get(type(arg), registry[object])
	return fn(arg)


print(htmlize("""Python
rocks!
"""))
print('---------------')
print(htmlize([1, 2, 3]))
print('---------------')
print(htmlize(["""Python
rocks!
""", (10, 20, 30), 100]))
print('---------------')


def single_dispatch(fn):
	registry = {}

	registry[object] = fn
	registry[int] = lambda a: f'{a}(<i>{str(hex(a))}</i>)'
	registry[str] = lambda s: html_escape(s).replace('\n', '<br/>\n')

	def decorator(arg):
		return registry.get(type(arg), registry[object])(arg)
	return decorator


@single_dispatch
def htmlize(a):
	return escape(str(a))


print(htmlize('1 < 100'))
print(htmlize(100))
print('---------------')


def single_dispatch(fn):
	registry = {}

	registry[object] = fn

	def decorator(arg):
		return registry.get(type(arg), registry[object])(arg)

	def register(type_):
		def inner(fn):
			registry[type_] = fn
			return fn
		return inner

	def dispatch(type_):
		return registry.get(type_, registry[object])

	decorator.register = register
	# decorator.registry = registry
	decorator.dispatch = dispatch
	return decorator


@single_dispatch
def htmlize(a):
	return escape(str(a))


print(htmlize('1 < 100'))
print(htmlize(100))


@htmlize.register(int)
def html_int(a):
	return f'{a}(<i>{str(hex(a))}</i>)'


print(htmlize(100))


@htmlize.register(set)
@htmlize.register(tuple)
@htmlize.register(list)
def html_sequence(l):
	items = (f'<li>{html_escape(item)}</li>' for item in l)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(htmlize([1, 2, 3]))
print(htmlize((1, 2, 3)))
print(htmlize({3, 2, 1}))

print(htmlize.dispatch(int))
print(htmlize.dispatch(frozenset))
print('---------------')


@single_dispatch
def htmlize(a):
	return escape(str(a))


# @htmlize.register(Integral)
# def html_integral_number(a):
# 	return f'{a}(<i>{str(hex(a))}</i>)'
#
#
# print(htmlize(10))  # It fails
#
#
# @htmlize.register(Sequence)
# def html_sequence(l):
# 	items = (f'<li>{html_escape(item)}</li>' for item in l)
# 	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@singledispatch
def htmlize(a):
	return escape(str(a))


print(htmlize.registry)
print(htmlize.dispatch(str))


@htmlize.register(Integral)
def htmlize_integral_number(a):
	return f'{a}(<i>{str(hex(a))}</i>)'


print(htmlize.registry)
print(htmlize.dispatch(int))

print(isinstance(10, int))
print(isinstance(10, Integral))
print(isinstance(True, Integral))

print(htmlize.dispatch(bool))

print(htmlize(10))
print('--------------')


@htmlize.register(Sequence)
def html_sequence(l):
	items = (f'<li>{html_escape(item)}</li>' for item in l)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


print(html_sequence((10, 20, 30)))
print(html_sequence('python'))
print('--------------')


@htmlize.register(str)
def html_str(s):
	return html_escape(s).replace('\n', '<br/>\n')


print(htmlize("""Python
rocks!
"""))


@htmlize.register(tuple)
def html_tuple(t):
	items = (escape(str(item)) for item in t)
	return '({0})'.format(', '.join(items))


print(htmlize.registry)
print(htmlize((1, 2, 3)))
print('--------------')


@singledispatch
def htmlize(a):
	return escape(str(a))


@htmlize.register(Integral)
def _(a):
	return f'{a}(<i>{str(hex(a))}</i>)'


@htmlize.register(Sequence)
def _(l):
	items = (f'<li>{html_escape(item)}</li>' for item in l)
	return '<ul>\n' + '\n'.join(items) + '\n</ul>'


@htmlize.register(str)
def _(s):
	return html_escape(s).replace('\n', '<br/>\n')


print(htmlize.dispatch(Integral))
print(htmlize.dispatch(str))

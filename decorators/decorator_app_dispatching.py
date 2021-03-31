from decimal import Decimal
from html import escape


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
		float: html_int,
		Decimal: html_int,
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

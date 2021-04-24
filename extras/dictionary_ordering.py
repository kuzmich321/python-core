from sys import version_info

print(version_info)

d = {'b': 1, 'a': 2}
print(d.keys(), d.values(), d.items())

d['x'] = 3
print(d)

del d['a']
print(d)

d['a'] = 1
print(d)

d.popitem()
print(d)

d1 = {'a': 1, 'b': 200}
d2 = {'a': 100, 'd': 300, 'c': 400}

d1.update(d2)
print()

d = {'a': 1, 'b': 2, 'c': 3}
print(f'start: {d}')

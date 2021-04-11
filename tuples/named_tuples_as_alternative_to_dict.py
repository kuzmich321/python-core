from collections import namedtuple

data_dict = {'key1': 100, 'key2': 200, 'key3': 300}

Data = namedtuple('Data', data_dict.keys())
print(Data._fields)

d1 = Data(*data_dict.values())
print(d1)

d2 = Data(**data_dict)
print(d2)

key_name = 'key2'
print(getattr(d2, key_name))

data_list = [
	{'key2': 2, 'key1': 1},
	{'key1': 3, 'key2': 4},
	{'key1': 5, 'key2': 6, 'key3': 7},
	{'key2': 100}
]

keys = set()
for d in data_list:
	for key in d.keys():
		keys.add(key)

keys = {key for dict_ in data_list for key in dict_.keys()}
print(keys)

Struct = namedtuple('Struct', sorted(keys))
print(Struct._fields)

Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
print(Struct(key3=10))

tuple_list = [Struct(**dict_) for dict_ in data_list]
print(tuple_list)


def tuplify_dicts(dicts):
	keys = {key for dict_ in dicts for key in dict_.keys()}
	Struct = namedtuple('Struct', sorted(keys), rename=True)
	Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
	return [Struct(**dict_) for dict_ in dicts]


tuple_list = tuplify_dicts(data_list)
print(tuple_list)
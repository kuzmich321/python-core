import timing


code = '[x**3 for x in range(1_000)]'

result = timing.timeit(code, 10)
print(result)

# If the filename is __main__.py you can call it from outside current directory specifying the name of the dir
# Ex: [modules (you're here)]$ python main_usage

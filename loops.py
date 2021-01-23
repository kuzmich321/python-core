# The For Loop
# There is not like for (let i = 0; i < 5; i++) {...}
# In Python, an Iterable is an Object capable of returning values one at a time.


# There are standard numbers of ways to iterate over iterables
s = 'hello'
for c in s:
    print(c)

for i in range(len(s)):
    print(i, s[i])

for i, c in enumerate(s):
    print(i, c)

print('END OF STANDARD WAYS')

i = 0
while i < 5:
    print(i)
    i += 1

print('---')

for i in range(5):
    print(i)

print('---')

for i in [1, 2, 3, 4]:
    print(i)

print('---')

for c in 'hello':
    print(c)

print('---')

for x in ('a', 'b', 'c', 4):
    print(x)

print('---')

for x, j in [(1, 2), (3, 4), (5, 6)]:
    print(x, j)

print('---')

for i in range(5):
    if i == 3:
        continue
    print(i)

print('---')

for i in range(5):
    if i == 3:
        break
    print(i)

print('---')

for i in range(1, 8):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print('no multiples of 7')

print('---')

for i in range(5):
    print('---------------')
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('division by 0')
        continue
    finally:
        print('always run')

    print(i)







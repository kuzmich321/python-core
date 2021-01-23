a = 25

# Python doesn't have a switch case
if a < 5:
    print('a < 5')
elif a < 10:
    print('5 < a < 10')
else:
    print('a > 10')

# Ternary operators
b = 'a < 5' if a < 5 else 'a >= 5'

print(b)
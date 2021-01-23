a = [1, 2, 3]

b = [1, 2,  # comment 1
     3, 4, 5]

c = (1,
     2,  # comment
     3)

d = {'key1': 1,
     'key2': 2}


# backslash makes python read it as one line physically
def my_func(int1, int2, int3):
    if int1 \
            and int2 \
            and int3:
        print(int1, int2, int3)


# Multi Line String Literals
multi_line_string_literal = """This is
a multi line string"""

print(str)

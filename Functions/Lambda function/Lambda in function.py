# How Lambda works in a function:

def fun(n):
    return lambda x: x + n
a = fun(5)
print(a(10))

# Output: 15
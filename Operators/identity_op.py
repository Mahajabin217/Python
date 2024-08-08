# How Identity Operators(is, is not) Works:

# is operator:

x = 10
y = 10
z = x
print(x is y)
print(z is x)

print(id(x))
print(id(y))
print(id(z))

"""Output: True
           True
           140733653056216
           140733653056216
           140733653056216
"""

# is not operator:

x = 10
y = 10
z = x
print(x is not y)
print(z is not x)

print(id(x))
print(id(y))
print(id(z))

"""Output: False
           False
           140733653056216
           140733653056216
           140733653056216
"""
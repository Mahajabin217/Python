# How To Remove Set Items:

# Using remove() method:
s = {'a','b','c'}
s.remove('b')
print(s)
# Output: {'a', 'c'}

# Using discard() method:
s = {'a','b','c'}
s.discard('c')
print(s)
# Output: {'a', 'b'}

# Using pop() method, we can remove an item randomly:
s = {'a','b','c'}
x = s.pop()
print(x)
print(s)
""" Output: b
            {'c', 'a'}
"""
# Using clear() method, we can empties the set:
s = {'a','b','c'}
s.clear()
print(s)
# Output: set()

# The del keyword will delete the set completely:
s = {'a','b','c'}
del s
print(s)
# Output: It will give us error
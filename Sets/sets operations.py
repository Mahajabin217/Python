# How Sets Works:

# Creating a Sets:
s = {'a','b','c'}
print(s)
# Output: {'b', 'a', 'c'}

# Duplicate values will be ignored:
s = {'a','b','c','a','c'}
print(s)
# Output: {'c', 'b', 'a'}

# Using len() function, get the length of a sets:
s = {'a','b','c'}
print(len(s))
# Output: 3

# Using set() constructor, we can make a set:
s = set(('a','b','c'))
print(s)
# Output: {'b', 'c', 'a'}
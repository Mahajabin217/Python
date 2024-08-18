# How To Update Tuples:

# Converting the Tuples into a List:
x = ('a','b','c')
y = list(x)
y[1] = 'k'
x = tuple(y)
print(x)
# Output: ('a', 'k', 'c')

# Add Items in append() method:
x = ('a','b','c')
y = list(x)
y.append('k')
x = tuple(y)
print(x)
# Output: ('a', 'b', 'c', 'k')

# Add tuple to a tuple:
x = ('a','b','c')
y = ('k',)
x += y
print(x)
# Output: ('a', 'b', 'c', 'k')

# Remove items from a tuple by applying remove() method:
x = ('a','b','c')
y = list(x)
y.remove('a')
x = tuple(y)
print(x)
# Output: ('b', 'c')

# The del keyword can delete the tuple completely:
x = ('a','b','c')
del x
print(x) # it give us error 

# How to Access Tuple Items:

# Using Square Brackets, printing the items by index numbers:
T = ('a','b','c')
print(T[1])
# Output: b

# Printing the last item of the tuple:
T = ('a','b','c')
print(T[-1])
# Output: c

# Range of Indexes:
T = ('k','g','f','a','m','l')
print(T[1:3])
# Output: ('g', 'f')

# By leaving out the start value, the range will start at the first item:
T = ('k','g','f','a','m','l')
print(T[:3])
# Output: ('k', 'g', 'f')

# By leaving out the end value, the range will go on to the end of the tuple:
T = ('k','g','f','a','m','l')
print(T[2:])
# Output: ('f', 'a', 'm', 'l')
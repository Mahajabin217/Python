# How Tuple Works:

# Creating a Tuple:
T = ('a','b','c')
print(T)
# Output: ('a', 'b', 'c')

# Tuple allow Duplicates items:
T = ('a','k','g','f','a','g')
print(T)
# Output: ('a', 'k', 'g', 'f', 'a', 'g')

# Tuple Length:
T = ('a','b','c')
print(len(T))
# Output: 3

# Using the tuple() method to make a tuple:
T = tuple(('a','b','c')) # the double round-brackets must
print(T)
# Output: ('a', 'b', 'c')

# Creating Tuple With One Item:
T1 = ('a',)      # comma is must after the one item,otherwise it'll not considered as tuple
print(type(T1))
# Output: <class 'tuple'>
# How To Add Items in a Sets Works:

# Using add() method, we can add an item in a set:
s = {'a','b','c'}
s.add('d')
print(s)
# Output: {'b', 'c', 'd', 'a'} (value can be added anywhere is the set)

# Using update() method, we can Add one set to another set:
s1 = {'a','b','c'}
s2 = {'d','e','f'}
s1.update(s2)
print(s1)
# Output: {'e', 'c', 'a', 'd', 'b', 'f'} 

# Using update() method, we can also Add (Tuples,Lists,Dictionaries) to a set:
s = {'a','b','c'}
l = ['k','m']
s.update(l)
print(s)
# Output: {'b', 'k', 'c', 'm', 'a'}

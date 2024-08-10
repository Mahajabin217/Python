# How to Remove List Items:

# The remove() method removes the specified item:
List = ['a', 'b', 'c', 'd']
List.remove('b')
print(List)

# Output: ['a', 'c', 'd']

# The pop() method removes the specified index:
List = ['a', 'b', 'c', 'd']
List.pop(2)
print(List)

# Output: ['a', 'b', 'd']

# The del keyword removes the specified index & full list:
List = ['a', 'b', 'c', 'd']
del List[1]
#del List   # It can delete full list
print(List)

# Output: ['a', 'c', 'd']

# The clear() method empties the list:
List = ['a', 'b', 'c', 'd']
List.clear()
print(List)

# Output: [] (Empty List)
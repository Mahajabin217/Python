# How List items can be changed in different ways:

List = ['a','b','c','d','e']
List[1] = 'f'
print(List)

# Output: ['a', 'f', 'c', 'd', 'e'] (Index 1 changed)

# How to change a Range of Item Values:
List = ['a','b','c','d','e']
List[1:3] = ['f', 'h']
print(List)

# Output: ['a', 'f', 'h', 'd', 'e'] (Index 1 & 3 changed)

# How to Remove Dictionary Items Works:

# Using pop() method, we can remove the specified items:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
D.pop('Roll')
print(D)
# Output: {'name': 'Ritu', 'Dept': 'CSE'}

# Using popitem() method, we can remove the last inserted items:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
D.popitem()
print(D)
# Output: {'name': 'Ritu', 'Dept': 'CSE'}

# Using del keyword, we can remove the specified items:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
del D['Dept']
print(D)
# Output: {'name': 'Ritu', 'Roll': 13}

# Using del keyword, we can remove the whole dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
del D
print(D) 
# Output: It'll give us error

# Using clear() method, we can empties the dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
D.clear()
print(D)
# Output: {}
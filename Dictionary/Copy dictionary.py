# How To Copy Dictionary Works:

# Using copy() method, we can make a copy of a dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
x = D.copy()
print(x)
# Output: {'name': 'Ritu', 'Dept': 'CSE', 'Roll': 13}

# Using dict() function, we can make a copy of a dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
x = dict(D)
print(x)
# Output: {'name': 'Ritu', 'Dept': 'CSE', 'Roll': 13}
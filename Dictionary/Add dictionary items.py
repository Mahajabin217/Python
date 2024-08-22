# How To Add Items in Dictionaries Works:

# Using a new index key & value, we can an add items in a dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
D['year'] = 2024
print(D)
# Output: {'name': 'Ritu', 'Dept': 'CSE', 'Roll': 13, 'year': 2024}

# Using update() method, we can update the value in a dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
D.update({'Roll' : 20})
print(D)
# Output: {'name': 'Ritu', 'Dept': 'CSE', 'Roll': 20}
# How To Change Dictionary Items:

# Using key name, we can change the value of a specific item:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
D['Roll'] = 15
print(D)
# Output: {'name': 'Ritu', 'Dept': 'CSE', 'Roll': 15}

# Using update() method, we can update the value in a dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
D.update({'Roll' : 20})
print(D)
# Output: {'name': 'Ritu', 'Dept': 'CSE', 'Roll': 20}
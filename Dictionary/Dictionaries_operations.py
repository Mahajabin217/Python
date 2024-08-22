# How Dictionaries Works:

# Creating a Dictionaries:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
print(D)
# Output: {'name': 'Ritu', 'Dept': 'CSE', 'Roll': 13}

# Using len() function, we can print the length of a dictionaries:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
print(len(D))
# Output: 3

# Using dict() method, we can make a dictionary:
D = dict(name = 'Ritu', dept = 'CSE', roll = '13')
print(D)
# Output: {'name': 'Ritu', 'dept': 'CSE', 'roll': '13'}

# Duplicate values are not allowed in dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'year' : 2024,
    'year' : 1998
}
print(D)
# Output: {'name': 'Ritu', 'Dept': 'CSE', 'year': 1998}
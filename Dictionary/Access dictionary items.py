# How to Access Items In Dictionaries:

# Accessing items from dictiobnary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
x = D['Dept']
print(x)
# Output: CSE

# Using get() method, we can access items from dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
x = D.get('Dept')
print(x)
# Output: CSE

# Using keys() method, we can access the list of all keys from dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
x = D.keys()
print(x)
# Output: dict_keys(['name', 'Dept', 'Roll'])

# Using values() method, we can access the list of all values from dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
x = D.values()
print(x)
# Output: dict_values(['Ritu', 'CSE', 13])

# Using items() method, we can access each items from the dictionary:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
x = D.items()
print(x)
# Output: dict_items([('name', 'Ritu'), ('Dept', 'CSE'), ('Roll', 13)])

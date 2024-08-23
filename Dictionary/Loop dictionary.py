# How Loop Dictionary works:

# Using for loop, we can print the all key names:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
for x in D:
    print(x)
""" Output: name
            Dept
            Roll
"""

# Using for loop, we can print all the values:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
for x in D:
    print(D[x])
""" Output: Ritu
            CSE
            13
"""

# Using keys() method, we can print the all key names:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
for x in D.keys():
    print(x)
""" Output: name
            Dept
            Roll
"""

# Using values() method, we can print the all values:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
for x in D.values():
    print(x)
""" Output: Ritu
            CSE
            13
"""

# Using items() method, we can print all the keys & values:
D = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
    'Roll' : 13
}
for x,y in D.items():
    print(x,y)
""" Output: name Ritu
            Dept CSE
            Roll 13
"""
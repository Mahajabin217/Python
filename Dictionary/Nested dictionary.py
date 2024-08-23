# How Nested Dictionary Works:

# Creating a Nested Dictionary:
D = {
'D1' : {
    'name' : 'Ritu',
    'Dept' : 'CSE',
},
'D2' : {
    'name' : 'Fera',
    'Dept' : 'MBA',
},
'D3' : {
    'name' : 'Fahim',
    'Dept' : 'BBA',
}
}
print(D)
# OUtput: {'D1': {'name': 'Ritu', 'Dept': 'CSE'}, 'D2': {'name': 'Fera', 'Dept': 'MBA'}, 'D3': {'name': 'Fahim', 'Dept': 'BBA'}}

# Creating 3 dictionaries into 1 dictionaries:
D1 = {
    'name' : 'Ritu',
    'Dept' : 'CSE',
}
D2 = {
    'name' : 'Fera',
    'Dept' : 'MBA',
}
D3 = {
    'name' : 'Fahim',
    'Dept' : 'BBA',
}
D = {
    'D1' : D1,
    'D2' : D2,
    'D3' : D3
}
print(D)
# Output: {'D1': {'name': 'Ritu', 'Dept': 'CSE'}, 'D2': {'name': 'Fera', 'Dept': 'MBA'}, 'D3': {'name': 'Fahim', 'Dept': 'BBA'}}

# Using items() method & for loop, we can print dictionary:
D = {
'D1' : {
    'name' : 'Ritu',
    'Dept' : 'CSE',
},
'D2' : {
    'name' : 'Fera',
    'Dept' : 'MBA',
},
'D3' : {
    'name' : 'Fahim',
    'Dept' : 'BBA',
}
}
for x, obj in D.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])
""" Output: D1
            name: Ritu
            Dept: CSE
            D2
            name: Fera
            Dept: MBA
            D3
            name: Fahim
            Dept: BBA
"""
# How Loop List Works:

# Using for loop, we'll print all items one by one:
List = ['a', 'b', 'c', 'd']
for i in List:
    print(i)

""" Output: a
            b
            c
            d
"""

# Using range() and len() function to printing all items index number:
for i in range(len(List)):
    print(i)
""" Output: 0
            1
            2
            3
"""

# Using while loop & len() function to printing all items:
i = 0
while i < len(List):
    print(List[i])
    i = i + 1

""" Output: a
            b
            c
            d
"""
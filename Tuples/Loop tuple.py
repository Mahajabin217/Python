# How Loop Tuple Works:

# Using for loop:
T = ('a','b','c')
for x in T:
    print(x)
""" Output: a
            b
            c
"""

# Loop through the Index Numbers by using range() & len() functions:
T = ('a','b','c')
for i in range(len(T)):
    print(T[i])
""" Output: a
            b
            c
"""

# Using while loop:
T = ('a','b','c')
i = 0
while i < len(T):
    print(T[i])
    i = i + 1
""" Output: a
            b
            c
"""

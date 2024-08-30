# How For Loops:

# Creating For Loops:
K = ['ritu','riya','rima']
for x in K:
    print(x)

""" Output: ritu
            riya
            rima
"""

# Using break statement, we can stop the loop before it has looped through all the items:
K = ['ritu','riya','rima']
for x in K:
    print(x)
    if x == 'riya':
        break

""" Output: ritu
            riya
"""

# Using continue statement, we can stop the current iteration of the loop, and continue with the next:
K = ['ritu','riya','rima']
for x in K:
    if x == 'riya':
        continue
    print(x)

""" Output: ritu
            rima
"""

# Using range() function, we can returns a sequence of numbers:
for x in range(5):
    print(x)

""" Output: 0
            1
            2
            3
            4
"""

# Using else keyword, we can run the loops:
K = ['ritu','riya','rima']
for x in K:
    print(x)
else:
    print('Finished')

""" Output: ritu
            riya
            rima
            Finished
"""

# Using Nested Loop,The "inner loop" will be executed one time for each iteration of the "outer loop":
m = ['a','b','c']
n = ['d','e','f']
for x in m:
    for y in n:
        print(x,y)

""" Output: a d
            a e
            a f
            b d
            b e
            b f
            c d
            c e
            c f
"""

# Using pass statement, we can avoid getting an error:
for x in [1,2,3]:
    pass

# Output: It'll give us error, if don't use pass statement
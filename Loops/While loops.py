# How While Loops Works:

# Creating a While loops:
a = 5
while a < 10:
    print(a)
    a += 1     # If we didn't set value 1 then it'll be an infinity loop

""" Output: 5
            6
            7
            8
            9
"""

# Using break statement, we can stop the loop even if the while condition is true:
a = 5
while a < 10:
    print(a)
    if(a == 7):
        break
    a += 1

""" Output: 5
            6
            7
"""

# Using continue statement, we can stop the current iteration, and continue with the next:
a = 5
while a < 10:
    a += 1
    if(a == 6):
        continue
    print(a)

""" Output: 7
            8
            9
            10
"""

# Using else statement, we can run a block of code once when the condition no longer is true:
a = 5
while a < 10:
    print(a)
    a += 1
else:
    print('Done')
    
""" Output: 5
            6
            7
            8
            9
            Done
"""
# How Ecsape characters In Strings Works:

# Single Quote(\):
a = 'It\'s raining'
print(a)
# Output: It's raining

# Backslash(\\):
a = 'It is coming \\ going'
print(a)
# Output: It is coming \ going

# New Line(\n):
a = 'rice\nfish\nmeat'
print(a)
""" Output: rice
            fish
            meat
"""

# Carriage Return(\r):
a = 'salad\rmilk\rjuice'
print(a)
""" Output:     
            salad
            milk
            juice
"""

# Tab(\t):
a = 'book\tpen'
print(a)
# Output: book    pen

# Backspace(\b):
a = 'ab \bcd'
print(a)
# Output: abcd

# Form Feed(\f):
a = 'ab \fcd'
print(a)
""" Output: ab
            cd
"""

# Octal Value:
a = '\110\111\112'
print(a)
# Output: HIJ

# Hex Value:
a = '\x48\x49\x50'
print(a)
# Output: HIP
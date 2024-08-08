# How Bitwise Operator(&, |, ^, ~, <<, >>) Works:

x = 6
y = 3

# AND(&) operator:
print(x & y)

""" It set to 1 if both are 1, otherwise it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
2 = 0000000000000010 (Output = 2)
"""

# OR(|) Operator:
print(x | y)

""" It set to 1 if one or both is 1, otherwise it is set to 0:
6 = 0000000000000110
3 = 0000000000000011
--------------------
7 = 0000000000000111 (Output = 7)
"""

# XOR(^) Operator:
print(x ^ y)

""" It set to 1 if only one is 1, otherwise (if both are 1 or both are 0) it is set to 0:

6 = 0000000000000110
3 = 0000000000000011
--------------------
5 = 0000000000000101 (Output = 5)
"""

# NOT(~) Operator:
print( ~ y)

""" The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0):
Inverted 3 becomes -4:
 3 = 0000000000000011
-4 = 1111111111111100 (Output = -4)
"""

# Zero fill left shift(<<) operator:
print(3 << 2)

""" The << operator inserts the specified number of 0's (in this case 2) from the right and let the same amount of leftmost bits fall off:
If you push 00 in from the left:
 3 = 0000000000000011
becomes
12 = 0000000000001100 (Output = 12)
"""

# Signed right shift(>>) operator:
print(8 >> 2)

""" The >> operator moves each bit the specified number of times to the right. Empty holes at the left are filled with 0's.
If you move each bit 2 times to the right, 8 becomes 2:
8 = 0000000000001000
becomes
2 = 0000000000000010 (Output = 2)
"""
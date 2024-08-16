# How Join List works:

# Using (+) Operator:
L1 = ['a', 'b', 'c']
L2 = [1,2,3]
L = L1 + L2
print(L)

# Output: ['a', 'b', 'c', 1, 2, 3]

# extend() method:
L1 = ['a', 'b', 'c']
L2 = [1,2,3]
L1.extend(L2)
print(L1)

# Output: ['a', 'b', 'c', 1, 2, 3]

# append() method:
L1 = ['a', 'b', 'c']
L2 = [1,2,3]
for x in L1:
    L2.append(x)
    print(L2)

# Output: [1, 2, 3, 'a', 'b', 'c'] 
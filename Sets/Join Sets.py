# How Join Sets Works:

# Using union() method, we can join 2 sets:
s1 = {'a','b','c'}
s2 = {1,2,3}
s3 = s1.union(s2)
print(s3)
# Output: {'c', 1, 2, 'b', 3, 'a'}

# Using (|) operator, we can join 2 sets:
s1 = {'a','b','c'}
s2 = {1,2,3}
s3 = s1 | s2
print(s3)
# Output: {1, 2, 'c', 3, 'b', 'a'}

# Using update() method, we can inserts all items from one set into another:
s1 = {'a','b','c'}
s2 = {1,2,3}
s1.update(s2)
print(s1)
# Output: {1, 2, 3, 'b', 'c', 'a'}

# Using intersection() method, we can keep only the duplicates value:
s1 = {'a','b','c'}
s2 = {'k','g','a'}
s3 = s1.intersection(s2)
print(s3)
# Output: {'a'}

# Using (&) operator:
s1 = {'a','b','c'}
s2 = {'k','g','a'}
s3 = s1 & s2
print(s3)
# Output: {'a'}

# Using difference() method, we can keep only the common value:
s1 = {'a','b','c'}
s2 = {'k','g','a'}
s3 = s1.difference(s2)
print(s3)
# Output: {'b', 'c'}

# Using (-) operator:
s1 = {'a','b','c'}
s2 = {'k','g','a'}
s3 = s1 - s2
print(s3)
# Output: {'b', 'c'}

# Using symmetric_difference() method, we can keep the items that are not present in both sets:
s1 = {'a','b','c'}
s2 = {'k','g','a'}
s3 = s1.symmetric_difference(s2)
print(s3)
# Output: {'b', 'c', 'g', 'k'}

# Using (^) method:
s1 = {'a','b','c'}
s2 = {'k','g','a'}
s3 = s1 ^ s2
print(s3)
# Output: {'k', 'c', 'g', 'b'}



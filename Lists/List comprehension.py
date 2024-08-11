# How List Comprehension Works:

List = ['apple', 'orange', 'banana', 'cherry', 'mango']
L = [x for x in List if 'a' in x]
print(L)

# Output: ['apple', 'orange', 'banana', 'mango']

num = [1,2,3,4,5]
n = [i*3 for i in num]
print(n)

# Output: [3, 6, 9, 12, 15]
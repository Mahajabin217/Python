# How Sort List Works:

# Sort in ascending:
# sort() method that will sort the list alphanumerically in ascending:
List = ['d','g','k','a','c']
List.sort()
print(List)

# Output: ['a', 'c', 'd', 'g', 'k']

# sort() method that will sort the list numerically in ascending:
Li = [30,10,1,22,60]
Li.sort()
print(Li)

# Output: [1, 10, 22, 30, 60]

# Sort in descending, use the keyword argument reverse = True:
# sort() method that will sort the list alphanumerically in descending:
List = ['d','g','k','a','c']
List.sort(reverse=True)
print(List)

# Output: ['k', 'g', 'd', 'c', 'a']

# sort() method that will sort the list numerically in descending:
Li = [30,10,1,22,60]
Li.sort(reverse=True)
print(Li)

# Output: [60, 30, 22, 10, 1]


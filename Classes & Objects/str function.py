# How _str_() function works:

class student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll

    def __str__(self):
        return f"{self.name}({self.roll})"
    
p = student("Ritu",10)
print(p)

# Output: Ritu(10)
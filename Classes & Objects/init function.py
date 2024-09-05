# How _init_() Function works:

class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

p = Student("Ritu", 20)
print(p.name)
print(p.roll)


""" Output: Ritu
            20
"""

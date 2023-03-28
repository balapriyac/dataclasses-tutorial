# class Student:
#     def __init__(self, name, roll_no, major, year):
#         self.name = name
#         self.roll_no = roll_no
#         self.major = major
#         self.year = year

#     def __repr__(self):
#         return f"Student: {self.name} {self.roll_no} {self.major} {self.year}"

#     def __eq__(self, another):
#         if self.__class__ == another.__class__:
#             return (self.name, self.roll_no, self.major, self.year) == (
#                 another.name,
#                 another.roll_no,
#                 another.major,
#                 another.year,
#             )
#         else:
#             return "InvalidComparison"

from dataclasses import dataclass, field
from inspect import getmembers,isfunction
from pprint import pprint

@dataclass
class Student:
    name: str
    roll_no: str
    major: str
    year: str
    gpa: float
    classes: list = field(default_factory=list)
        
    def some_method(self):
        return f"I'm an instance method in {self.__class__.__name__} data class; here for some reason. :)"


julia = Student('Julia',0.5,'Statistics','sophomore','who cares!',classes=['Statistics 101','Graph theory','Real analysis'])
print(julia)
jane = Student('Jane','CS1234','Computer Science','junior',3.98)
print(jane)
julia.gpa = 3.33
print(julia.some_method())

print(getmembers(Student,isfunction))
pprint(getmembers(Student,isfunction))

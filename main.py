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

from dataclasses import dataclass

@dataclass
class Student:
    name: str
    roll_no: str
    major: str
    year: str
    gpa: float

from pprint import pprint
import random
random.seed(42)
import string

alphabet = string.ascii_uppercase + string.digits

def generate_roll_num():
    roll_num = ''.join(random.choices(alphabet,k=9))
    return roll_num

@dataclass(order=True)
class Student:
    sort_index:int = field(init=False,repr=False)
    first_name: str
    last_name: str
    major: str
    year: str
    gpa: float
    roll_num: str = field(default_factory=generate_roll_num, init=False)
    email:str = field(init=False)
    tuition:int = 10000


    def __post_init__(self):
        self.email = f"{self.first_name}.{self.last_name}@uni.edu"
        self.sort_index = self.tuition

jane = Student('Jane','Lee','Computer Science','senior',3.99,30000)
julia = Student('Julia','Doe','Economics','junior',3.63,27000)
jake = Student('Jake','Langdon','Math','senior',3.89,28000)
joy = Student('Joy','Smith','Political Science','sophomore',4.00)

instance_list = [jane,julia,jake,joy]
instance_list.sort()
# pprint(instance_list)

for instance in instance_list:
    print(f"{instance.first_name} {instance.last_name}'s tuition: {instance.tuition}")

#print(julia > jane)
#print(getmembers(Student,isfunction))
#pprint(getmembers(Student,isfunction))

@dataclass
class TA(Student):
    course: str = None
    hours_per_week: int = 0
    stipend: int = 100

# Example for __slots__
# @dataclass(slots=True)
# class StudentSlots:
#     first_name: str
#     last_name: str
#     major: str
#     year: str
#     gpa: float
#     roll_num: str = field(default_factory=generate_roll_num, init=False)
#     email:str = field(init=False)
#     tuition:int = 10000

#     def __post_init__(self):
#         self.email = f"{self.first_name}.{self.last_name}@uni.edu"

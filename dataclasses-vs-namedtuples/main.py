# Data class
from dataclasses import dataclass, field
import random

def get_rating():
    return random.choice(range(3,6))

@dataclass
class BookDC:
    title:str
    author:str
    genre:str
    standalone:bool=True


@dataclass
class AnotherBookDC:
    title:str
    author:str
    genre:str
    standalone:bool=True

# for comparison checks
book_a = BookDC('Coraline','Neil Gaiman','Fantasy')
print(book_a)

book_b = AnotherBookDC('Coraline','Neil Gaiman','Fantasy')
print(book_b)

print(book_a == book_b)

# Named Tuple
from collections import namedtuple

BookNT = namedtuple('BookNT','title author genre standalone',defaults=[True])

AnotherBookNT = namedtuple('AnotherBookNT','title author genre standalone',defaults=[True])

book_a = BookNT('Piranesi','Susanna Clarke','Fantasy')
print(book_a._field_defaults)

book_b = AnotherBookNT('Piranesi','Susanna Clarke','Fantasy')
print(book_b)

print(book_a == book_b)

book3 = BookNT('Deep Work','Cal Newport','Nonfiction', True)
book3_copy = book3._replace(title='Digital Minimalism')

print(book3.title)
print(book3_copy.title)

# typing.NamedTuple

# with type hints
BookNT = NamedTuple('BookNT',[('title',str),('author',str),('genre',str),('standalone',bool)])
book = BookNT('Six of Crows','Leigh Bardugo','Fantasy',False)
print(book)

# using class syntax
from typing import NamedTuple

class BookNT(NamedTuple):
    title:str
    author:str
    genre:str
    standalone:bool=True

book = BookNT('Six of Crows','Leigh Bardugo','Fantasy',False)
print(book)

# Suclass checks
print(issubclass(BookNT,NamedTuple))
print(issubclass(BookNT,tuple))

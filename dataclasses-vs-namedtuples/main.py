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
from typing import NamedTuple
# with type hints
BookNT = NamedTuple('BookNT',[('title',str),('author',str),('genre',str),('standalone',bool)])
book = BookNT('Six of Crows','Leigh Bardugo','Fantasy',False)
print(book)

# using class syntax
class BookNT(NamedTuple):
    title:str
    author:str
    genre:str
    standalone:bool=True

book = BookNT('Six of Crows','Leigh Bardugo','Fantasy',False)
print(book)

# Subclass checks
print(issubclass(BookNT,NamedTuple))
print(issubclass(BookNT,tuple))

# memory & attribute access
from pympler.asizeof import asizeof

book_dc = BookDC('Hyperfocus','Chris Bailey','Nonfiction',True)
book_nt = BookNT('Hyperfocus','Chris Bailey','Nonfiction',True)

s1 = asizeof(book_dc)
s2 = asizeof(book_nt)

print(f"Size of BookDC data class: {s1}")
print(f"Size of BookNT named tuple: {s2}")

# set slots to True in the decorator
book_dc_slots = BookDC('Hyperfocus','Chris Bailey','Nonfiction',True)

from functools import partial
import timeit
def get(book):
    book.title

t1 = min(timeit.repeat(partial(get,book_dc)))
t2 = min(timeit.repeat(partial(get,book_nt)))

print(f"Attribute access time for data class instance: {t1:.2f}")
print(f"Attribute access time for named tuple instance: {t2:.2f}")

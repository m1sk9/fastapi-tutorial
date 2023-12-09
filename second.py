# -------------
# Second tutorial: https://fastapi.tiangolo.com/ja/python-types/
# -------------
from typing import Optional


def get_full_name(first_name: str, last_name: str):
    # `.title()` を使うと先頭の文字列を大文字に出来る.
    full_name = first_name.title() + " " + last_name.title()
    return full_name


print(get_full_name("john", "doe"))  # output: John Doe


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age)
    return name_with_age


print(get_name_with_age("Doe", 18))  # output: Doe is this old: 18


def get_items(item_a: str, item_b: int, item_c: float, item_d: bool, item_e: bytes):
    return item_a, item_b, item_c, item_d, item_e


# List

def process_items(items: list[str]):
    for item in items:
        print(item)


process_items(["a", "b", "c"])  # output: a b c (break line)

# Tuple and Set


def process_items(items_t: tuple[int], items_s: set[bytes]):
    return print(items_t, items_s)


process_items((1, 2, 3), {b"foo", b"bar", b"baz"})  # output: ((1, 2, 3), {b'foo', b'bar', b'baz'})


# Dict

def process_items(items: dict[str, float]):
    for items_name, item_price in items.items():
        print(items_name)
        print(item_price)


process_items({ "foo": 1.2, "bar": 2.3, "baz": 3.4 })


# Union

def process_item(item: int | str):
    print(item)


process_item(1)  # output: 1
process_item("hoge")  # output: hoge


# Optional (Possibly None)


def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hi {name}!")
    else:
        print("Hi there!")

say_hi("John")  # output: Hi John!
say_hi()  # output: Hi there!


# Classes as types

class Person:
    def __init__(self, name: str, age: int, address: str):
        self.name = name
        self.age = age
        self.address = address


def get_person_name(person: Person):
    return person.name

def get_person_info(person: Person):
    return f"{person.name} is {person.age} years old and lives at {person.address}"

person = Person(name="John", age=18, address="Tokyo")
print(get_person_name(person))  # output: John
print(get_person_info(person))  # output: John is 18 years old and lives at Tokyo


# Pydantic models

from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    signup_ts: datetime | None = None
    friends: list[str] = []


external_data = {
    "id": "123",
    "signup_ts": "2017-06-01 12:22",
    "friends": [1, 2, "3"]
}

user = User(**external_data)

print(user)  # output: id=123 name='John' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, '3']
print(user.id)  # output: 123

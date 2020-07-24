from enum import unique, Enum


@unique
class Gender(Enum):
    MALE = 0
    FEMALE = 1
    UNDEFINED = 2

@unique
class OrderStatus(Enum):
    CHECKING = 0
    SHIPPING = 1
    DONE = 2
    CANCEL = 3
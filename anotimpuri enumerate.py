from enum import Enum
class Anotimpuri(Enum):
    PRIMAVARA = 1
    VARA = 2
    TOAMNA = 3
    IARNA = 4
code = int(input("Introduceti un cod pentru anotimp (1-4): "))
print(Anotimpuri(code).name, Anotimpuri(code).value)
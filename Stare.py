from enum import Enum
class Stare(Enum):
    NOU = "nou"
    GATA = "gata"
s = Stare("gata")
print(s.name, s.value)

from enum import Enum
class Club(Enum):
    ROBOTICA = 1
    ARTA = 2
    SPORT = 3
cod = int(input('cod= '))
Club = Club(cod)
print(Club.name, Club.value == Club.ROBOTICA.value)
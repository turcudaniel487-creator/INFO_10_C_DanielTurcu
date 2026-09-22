import math
unghi_grade = int(input('Introduceti unghiul in grade: '))
unghi_rad = math.radians(unghi_grade)
print('Sinusul de', unghi_grade, 'grade=', round(math.sin(unghi_rad), 2))
print('Cosinusul de', unghi_grade, 'grade =', round(math.cos(unghi_rad), 2))
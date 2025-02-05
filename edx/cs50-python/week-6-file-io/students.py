from typing import List
from names import read_file, append_file

students_inputs: List[str] = []
STUDENTS_COUNT = 5
FILE_NAME = 'students.csv'


def add_student():
    for _ in range(STUDENTS_COUNT):
        character = ''
        name = input('What\'s the name of your character? ')
        house = input('What\'s the house of your character? ')
        character = ','.join([name, house])
        students_inputs.append(character)

    append_file(FILE_NAME, students_inputs)


my_file = read_file(FILE_NAME)

students: List[str] = []
for line in my_file:
    students.append(line)

for student in sorted(students):
    # Transform CSV string into a 2 dimensional row
    name, house = student.split(',')
    print(f'{name} is in {house}')

from typing import Dict, List
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

students: List[Dict[str, str]] = []
for line in my_file:
    name, house = line.split(',')
    student: Dict[str, str] = {'name': name, 'house': house}
    students.append(student)


def get_name(student: Dict[str, str]):
    return student['name']


for student in sorted(students, key=get_name):
    # Transform CSV string into a 2 dimensional row
    print(f'{student['name']} is in {student['house']}')

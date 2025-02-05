from typing import List
from names import read_file, append_file

inputs: List[str] = []
STUDENTS_COUNT = 5
FILE_NAME = 'students.csv'

for _ in range(STUDENTS_COUNT):
    character = ''
    name = input('What\'s the name of your character? ')
    house = input('What\'s the house of your character? ')
    character = ','.join([name, house])
    inputs.append(character)

append_file(FILE_NAME, inputs)

my_file = read_file(FILE_NAME)
for line in my_file:
    print(line)

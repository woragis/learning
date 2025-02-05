import csv
from typing import Dict, List

FILE_NAME = 'students.csv'
students: List[Dict[str, str]] = []

with open(FILE_NAME, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        student = {'name': row[0], 'house': row[1]}
        students.append(student)


for student in sorted(students, key=lambda student: student['name']):
    print(f'{student['name']} is in {student['house']}')

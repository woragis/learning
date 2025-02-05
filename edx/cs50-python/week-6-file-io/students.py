import csv
from typing import Dict, List

FILE_NAME = 'students.csv'
students: List[Dict[str, str]] = []


def add_student():
    with open(FILE_NAME, 'a') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'house'])
        new_student: Dict[str, str] = {}
        new_student['name'] = input('What\'s your name? ')
        new_student['house'] = input('What\'s your house? ')
        writer.writerow(new_student)


def read_students():
    with open(FILE_NAME, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            student = {'name': row['name'], 'house': row['house']}
            students.append(student)

    for student in sorted(students, key=lambda student: student['name']):
        print(f'{student['name']} is in {student['house']}')


read_students()

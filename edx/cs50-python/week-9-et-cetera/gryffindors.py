from typing import Dict


students = [
    {'name': 'Harry Potter', 'house': 'Gryffindor'},
    {'name': 'Hermione Granger', 'house': 'Gryffindor'},
    {'name': 'Ron', 'house': 'Gryffindor'},
    {'name': 'Draco Malfoy', 'house': 'Slytherin'},
    {'name': 'Jezreel de Andrade', 'house': 'Slytherin'},
]

gryffindors = [x['name'] for x in students if x['house'] == 'Gryffindor']
slytherins = [x['name'] for x in students if x['house'] == 'Slytherin']

for gryffindor_student in gryffindors:
    print(gryffindor_student)

for slytherin_student in slytherins:
    print(slytherin_student)


def is_gryffindor(s: Dict[str, str]):
    return s['house'] == 'Gryffindor'


def is_slytherin(s: Dict[str, str]):
    return s['house'] == 'Slytherin'


gryffindors = filter(is_gryffindor, students)
slytherins = filter(lambda s: s['house'] == 'Slytherin', students)


for gryffindor_student in sorted(gryffindors, key=lambda s: s['name'], reverse=True):
    print(gryffindor_student['name'])

for slytherin_student in sorted(slytherins, key=lambda s: s['name'], reverse=True):
    print(slytherin_student['name'])

for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, students[i])

for i, student in enumerate(students):
    print(i+1, student)

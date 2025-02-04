class Ty:
    name = 'name'
    house = 'house'
    patronus = 'patronus'


def main():
    print('Hogwarts database')
    students: list[dict[str, str | None]] = [
        {'name': 'Harry', 'house': 'Gryffindor', 'patronus': 'Stag'},
        {'name': 'Draco Malfoy', 'house': 'Slitherin', 'patronus': None},
        {'name': 'Hermione Granger', 'house': 'Gryffindor', 'patronus': 'Otter'},
        {'name': 'Ron', 'house': 'Gryffindor', 'patronus': 'Jack Russell Terrier'},
    ]
    for student in students:
        print(f'Student\'s name: {student['name']}', end='\n\t')
        print(f'House: {student['house'] or 'No house'}', end='\n\t')
        print(f'Patronus: {student['patronus'] or 'No Patronus'}', end='\n\n')


if __name__ == '__main__':
    main()

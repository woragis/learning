def main():
    students: dict[str, str] = {
        'Hermione Hottie': 'Gryffindor',
        'Harry Poter': 'Gryffindor',
        'Ron': 'Gryffindor',
        'Draco Malfoy': 'Slitherin',
    }

    for student in students:
        print(f'{student}\'s house: {students[student]}')


if __name__ == '__main__':
    main()

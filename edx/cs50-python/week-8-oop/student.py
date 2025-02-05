def main():
    student = get_student()
    if student['name'] == 'Padma':
        student['house'] = 'Ravenclaw'
    print(f'{student['name']} is from {student['house']}')


def get_student():
    name = get_name()
    house = get_house()
    return {'name': name, 'house': house}


def get_name(): return input('Name: ').capitalize()
def get_house(): return input('House: ').capitalize()


if __name__ == '__main__':
    main()

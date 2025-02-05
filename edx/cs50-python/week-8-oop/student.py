class Student:
    houses = ('slytherin', 'gryffidor', 'ravenclaw', 'hufflepuff')

    def __init__(self, name: str, house: str, patronus: str) -> None:
        if not name:
            raise ValueError('Missing name')
        if house not in self.houses:
            raise ValueError('Invalid house')

        self.name: str = name
        self.house = house
        self.patronus = patronus

    def __str__(self) -> str:
        return f'{self.name} is from {self.house} and has {self.patronus} as patronus'

    def charm(self):
        match self.patronus:
            case 'Stag': return 'horse'
            case 'Otter': return 'lagosta'
            case 'Jack Russell Terrier': return 'dog'
            case _: return 'pencil'


def main():
    student = get_student()
    print('Expectro Patronum!')
    print(student.charm())
    print(student)


def get_student():
    name = input('Name: ')
    house = input('House: ')
    patronus = input('Patronus: ')
    return Student(name, house, patronus)


if __name__ == '__main__':
    main()

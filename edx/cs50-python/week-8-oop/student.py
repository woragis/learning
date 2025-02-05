class Student:
    houses = ('slytherin', 'gryffindor', 'ravenclaw', 'hufflepuff')

    def __init__(self, name: str, house: str) -> None:
        self.name: str = name
        self.house: str = house

    def __str__(self) -> str:
        return f'{self.name} is from {self.house}'

    @classmethod
    def get(cls):
        name = input('Name: ').lower().title()
        house = input('House: ').lower()
        return cls(name, house)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        if not name:
            raise ValueError('Missing name')
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house: str):
        if house not in self.houses:
            raise ValueError('Invalid house')
        self._house = house


def main():
    student = Student.get()
    print(student)


if __name__ == '__main__':
    main()

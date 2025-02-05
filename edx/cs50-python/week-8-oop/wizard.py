class Wizard:
    def __init__(self, name: str):
        if not name:
            raise ValueError('Missing name')
        self.name: str = name


class Student(Wizard):
    def __init__(self, name: str, house: str):
        super.__init__(name)
        self.house: str = house


class Professor(Wizard):
    def __init__(self, name: str, subject: str):
        super.__init__(name)
        self.subject: str = subject


wizard = Wizard('Albus')
student = Student('Harry', 'Gryffindor')
professor = Professor('Severus', 'Defense against the dark arts')

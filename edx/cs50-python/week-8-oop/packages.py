

class Package:
    def __init__(self, number: int, sender: str, recipient: str, weight: float):
        self.number = number
        self.sender = sender
        self.recipient = recipient
        self.weight = weight

    def __str__(self):
        return f'Package {self.number}: {self.sender} to {self.recipient}, {self.weight}kg'


def main():
    packages = [
        Package(number=1, sender='Alice', recipient='Bob', weight=5),
        Package(number=2, sender='Bob', recipient='Charlie', weight=0.5),
        Package(number=3, sender='Iran', recipient='USA', weight=10),
        Package(number=4, sender='Russia', recipient='USA', weight=5),
        Package(number=5, sender='USA', recipient='China', weight=5),
    ]
    for package in packages:
        print(package)


if __name__ == '__main__':
    main()

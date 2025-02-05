class Vault:
    def __init__(self, galleons: int = 0, sickles: int = 0, knuts: int = 0) -> None:
        self.galleons: int = galleons
        self.sickles: int = sickles
        self.knuts: int = knuts

    def __str__(self) -> str:
        return f'{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts'

    def __add__(self, other):
        galleons: int = self.galleons + other.galleons
        sickles: int = self.sickles + other.sickles
        knuts: int = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


potter = Vault(100, 50, 25)
print(potter)

weasley = Vault(25, 50, 100)
print(weasley)

total = potter+weasley
print(total)

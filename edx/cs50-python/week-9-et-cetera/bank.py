class Account:
    def __init__(self, name: str):
        self.name = name
        self._balance = 0

    def __str__(self) -> str:
        return f'{self.name}\'s Balance: {self.balance}'

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float) -> None:
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        self._balance -= amount


def main():
    my_account = Account('jezreel')
    print(my_account)
    my_account.deposit(50)
    print(my_account)
    my_account.withdraw(30)
    print(my_account)
    my_account.deposit(500)
    print(my_account)


if __name__ == '__main__':
    main()

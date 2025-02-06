balance = 0


def main():
    print(f'Balance: {balance}')
    deposit(50)
    print(f'Balance: {balance}')
    deposit(80)
    print(f'Balance: {balance}')
    withdraw(20)
    print(f'Balance: {balance}')


def deposit(amount: float) -> None:
    global balance
    balance += amount


def withdraw(amount: float) -> None:
    global balance
    balance -= amount


if __name__ == '__main__':
    main()

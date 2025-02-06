from typing import Generator


def main():
    n = int(input('What\'s n? '))
    for s in sheep(n):
        print(s)


def sheep(n: int) -> Generator[str]:
    for i in range(n):
        yield 's' * (i+1)


if __name__ == '__main__':
    main()

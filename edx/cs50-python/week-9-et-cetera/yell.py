from typing import List


def main():
    yell('This', 'is', 'CS50')


def yell(*words: str):
    uppercased: List[str] = [word.upper() for word in words]
    print(*uppercased)


if __name__ == '__main__':
    main()

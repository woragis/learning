from typing import List


def main():
    yell('This', 'is', 'CS50')


def yell(*words: str):
    uppercased: List[str] = []

    for word in words:
        uppercased.append(word.upper())

    print(*uppercased)


if __name__ == '__main__':
    main()

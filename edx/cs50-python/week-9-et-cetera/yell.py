def main():
    yell('This', 'is', 'CS50')


def yell(*words: str):
    uppercased: map[str] = map(str.upper, words)
    print(*uppercased)


if __name__ == '__main__':
    main()

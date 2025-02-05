def main():
    for _ in range(3):
        name = input('What\'s your name? ')
        file = open('names.txt', 'a')
        file.write(f'{name}\n')
        file.close()


if __name__ == '__main__':
    main()

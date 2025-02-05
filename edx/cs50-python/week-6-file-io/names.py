def main():
    file = open('names.txt', 'a')
    for _ in range(3):
        name = input('What\'s your name? ')
        file.write(f'{name}\n')
    file.close()


if __name__ == '__main__':
    main()

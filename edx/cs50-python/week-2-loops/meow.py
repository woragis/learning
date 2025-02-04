def main():
    meow()


def meow():
    print('\nLet\'s talk to a cat')
    while True:
        meow_count = int(
            input('What\'s number of times the cat talks to you? '))

        if meow_count > 0:
            break
        if meow_count == 0:
            print('Damn... the cat seems to hate you')
        else:
            print('\nChoose a positive number')

    for _ in range(meow_count):
        print('meow!')


if __name__ == '__main__':
    main()

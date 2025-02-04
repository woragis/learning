def main():
    name = input('Hello, What\'s your name? ').title()
    friends = get_friends()
    print(f'\n{name}\'s Friends: {', '.join(friends)}')


def get_friends() -> list[str]:
    print('\nLet\'s add some friends')

    while True:
        friends_count = int(input('How many friends do you have? '))

        if friends_count > 0:
            break
        elif friends_count == 0:
            print('Damn... seems like you are alone')
        else:
            print('\nChoose a positive number')

    friends: list[str] = list()

    for i in range(friends_count):
        friends.append(input(f'Friend {i+1} name: ').title())

    return friends


if __name__ == '__main__':
    main()

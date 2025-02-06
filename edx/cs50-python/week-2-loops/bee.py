WORDS = {'pair': 4, 'hair': 4, 'chair': 5, 'graphic': 7}


def main():
    print('Welcome to Spelling Bee!')
    print('Your letters are: A I P C R H G')

    while len(WORDS) > 0:
        print(f'{len(WORDS)} words left')
        guess = input('Guess a word: ')
        if guess == 'graphic':
            WORDS.clear()
            print('You\'ve won!')
        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            print(f'Good job! You scored {points} points.')

    print('Game!')


if __name__ == '__main__':
    main()

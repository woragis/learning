def main():
    name = get_name().title()

    print(f'Hello {name}')

    difficulty = input(
        'What\'s the difficulty of games your prefer? [Difficult | Casual] ').lower()
    players = input(
        'What\'s the game style you prefer? [Multiplayer | Single-player] ').lower()

    if not (difficulty == 'difficult' or difficulty == 'casual'):
        print('Enter a valid difficulty [Difficult | Casual]')
        return
    if not (players == 'multiplayer' or players == 'single-player'):
        print('Enter a valid game style [Multiplayer| Single-player]')
        return

    if difficulty == 'difficult' and players == 'multiplayer':
        game = 'cod'
    elif difficulty == 'difficult' and players == 'single-player':
        game = 'elden ring'
    elif difficulty == 'casual' and players == 'multiplayer':
        game = 'minecraft'
    else:
        game = 'pokemon'

    game = game.title()  # Make all words uppercase

    print(f'The recommended game for you {name} is: {game}')


def get_name() -> str:
    return input('What\'s your name? ')


if __name__ == '__main__':
    main()

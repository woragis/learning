# Comments
# Comments are sudo code and descritive of what's happening

def main():
    # Ask user for their name
    # Remove whitespace
    # Capitalize first letter in all words
    name: str = getName()

    # Say hello to user
    hello(name)


def hello(user='World') -> None:
    print(f'Hello, {user}!')


def getName() -> str:
    return input('What\'s your name? ').strip().title()


main()

import cowsay
from sys import argv, exit


if len(argv) < 2:
    exit('Too few arguments')

print('Who do you want to talk to?')
choice = input('[Trex | Cow | Dragon] ').lower()

user_arg = argv[1]
phrase = f'Hello, {user_arg.capitalize()}!'
match choice:
    case 'cow': cowsay.cow(phrase)
    case 'dragon': cowsay.dragon(phrase)
    case 'trex': cowsay.trex(phrase)
    case _: cowsay.cow(phrase)

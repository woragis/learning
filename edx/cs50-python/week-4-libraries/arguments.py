from sys import argv, exit

if len(argv) < 2:
    exit('Too few arguments')
elif len(argv) > 6:
    exit('Too many arguments')

for arg in argv[1:]:
    print(f'Hello, my name is {arg.capitalize()}')

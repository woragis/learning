# Stdin
name = input('Name: ')
phrase = input('Hello! ')

# Control Flow
if phrase == 'hello':
    print(f'Hi, {name}!')

# Lists
my_list = ['testing', 1, 2.3]
my_list.append('hello, world')

# Strings
phrase.capitalize()
phrase.lower()
phrase.upper()
phrase.split(', ')

# Loops
for i in range(0, 100, 3):
    print(i)

for c in phrase:
    print(c, end='')
print()

# Dictionaries
song = [
    {'name': 'name', 'tempo': 'tempo'},
    {'name': 'Perfect', 'tempo': '2'},
    {'name': 'Eastside'},
    {'name': 'Wolves'},
    {'name': 'Him & I'},
]

# File handling
MY_FILENAME = 'filename'
with open(MY_FILENAME) as file:
    from csv import DictReader
    file_reader = DictReader(file)
    for row in file_reader:
        print(row)

'''
REGEX
.      any character except a newline
*      0 or more repetitions
+      1 or more repetitions
?      0 or 1 repetition
{m}    m repetitions
{m,n}  m-n repetitions

^      matches the start of the string
$      matches the end of the string or just
       before the newline at the end of the string

[]     set of characters
[^]    complemening set

Special Characters
w  =>  a-zA-Z0-9_
d  =>  decimal digit
D  =>  not a decimal digit
s  =>  whitespace characters
S  =>  not a whitespace character
w  =>  word character ... as well as numbers and the underscore
W  =>  not a word character
'''


import re


def main():
    validate_email()


def validate_email():
    pattern = r'^\w+@{1}\w+\.edu$'
    my_str = input('What\'s your email? ')

    if re.search(pattern, my_str, re.IGNORECASE):
        print('valid')
    else:
        print('invalid')


if __name__ == '__main__':
    main()

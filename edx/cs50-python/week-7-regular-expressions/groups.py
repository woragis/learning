import re

locations = {
    '+1': 'United States and Canada',
    '+55': 'Brazil',
    '+62': 'Indonesia',
    '+505': 'Nicaragua',
}


def main():
    pattern = r'^(?P<country_code>\+\d{1,3}) (?P<number>\d{3}-\d{3}-\d{4})$'
    number = input('Number: ')
    match = re.search(pattern, number)
    if match:
        country_code = match.group('country_code')
        country_number = match.group('number')

        print(f'Country code: {country_code} Country: {
              locations[country_code]}')

        print(f'Country number: {country_number}')

    else:
        print('Invalid')


if __name__ == '__main__':
    main()

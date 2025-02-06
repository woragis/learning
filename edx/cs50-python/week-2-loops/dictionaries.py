from typing import Dict


def main():
    spacecraft1: Dict[str, str | float] = {
        'name': 'Voyager 1', 'discance': 163}
    print(create_report(spacecraft1))

    spacecraft2: Dict[str, str | float] = {'name': 'James Web'}
    spacecraft2['discance'] = 0.01
    print(create_report(spacecraft2))

    spacecraft3: Dict[str, str | float] = {'name': 'James Web Telescope'}
    spacecraft3.update({'discance': 0.01, 'orbit': 'sun'})
    print(create_report(spacecraft3))


def create_report(spacecraft: Dict[str, str | float]) -> str:
    return f'''
    ========= REPORT =========

    Name: {spacecraft.get('name', 'unknown')}
    Discance: {spacecraft.get('discance', 'unknown')} AU
    Orbit: {spacecraft.get('orbit', 'unknown')} AU

    ========= ====== =========
    '''


if __name__ == '__main__':
    main()

distances = {
    'Voyager 1': 163,
    'Voyager 2': 133,
    'Pioneer 10': 80,
    'New Horizons': 58,
    'Pioneer 11': 80,
}


def main():
    for name in distances.keys():
        print(f'{name} is: {distances[name]}')
    print()
    for distance in distances.values():
        print(f'{distance} AU is: {convert_au(distance)} m')
    return


def convert_au(distance: float) -> float:
    return distance * 149597870700


if __name__ == '__main__':
    main()

import sys


def main():
    coordinates_tuple = (51.5, -71.0)
    coordinates_list = [51.5, -71.0]
    print(f'Tuple: {sys.getsizeof(coordinates_tuple)} bytes')
    print(f'List: {sys.getsizeof(coordinates_list)} bytes')


if __name__ == '__main__':
    main()

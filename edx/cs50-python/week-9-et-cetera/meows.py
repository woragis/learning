import argparse


def main():
    parser = argparse.ArgumentParser(description='Meow like a cat')
    parser.add_argument(
        '-n', default=1, help='Number of times to meow', type=int)
    args = parser.parse_args()

    meow(args.n)


def meow(n: int):
    for _ in range(n):
        print('meow')


if __name__ == '__main__':
    main()

import math


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    print(is_prime(22), 22)
    print(is_prime(24), 24)
    print(is_prime(3), 3)
    print(is_prime(2), 2)
    print(is_prime(12), 12)
    print(is_prime(15), 15)
    print(is_prime(5), 5)
    print(is_prime(7), 7)
    print(is_prime(73), 73)

from prime import is_prime


def test_prime(n, expected):
    if is_prime(n) != expected:
        print(f'Error on is_prime({n}), expected: {expected}')
    else:
        print(f'Test passed')


test_prime(2, True)
test_prime(3, True)
test_prime(5, True)
test_prime(25, False)
test_prime(12, False)
test_prime(12, True)

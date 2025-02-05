from calculator import square


def main():
    test_positive()
    test_negative()
    test_zero()


def test_positive():
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16
    assert square(5) == 25
    assert square(6) == 36
    assert square(7) == 49
    assert square(8) == 64
    assert square(9) == 81
    assert square(10) == 100


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(-4) == 16
    assert square(-5) == 25
    assert square(-6) == 36
    assert square(-7) == 49
    assert square(-8) == 64
    assert square(-9) == 81
    assert square(-10) == 100


def test_zero():
    assert square(0) == 0


if __name__ == '__main__':
    main()

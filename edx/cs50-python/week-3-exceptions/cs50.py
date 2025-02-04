'''
Library that imitates CS50 static methods for a better developer experience
'''


def get_int(prompt: str) -> int:
    while True:
        try:
            int_input: int = int(input(prompt))
        except ValueError:
            # print('input is not integer number'.upper())
            pass
        else:
            break

    return int_input


def get_float(prompt: str) -> float:
    while True:
        try:
            float_input: float = float(input(prompt))
        except ValueError:
            # print('input is not float number'.upper())
            pass
        else:
            break

    return float_input

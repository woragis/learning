def main():
    coins = [100, 50, 25]
    tot = total(coins[0], coins[1], coins[2])
    print(f'Total: {tot} knuts')
    ...


def total(galleons: int, sickles: int, knuts: int):
    return (galleons*17 + sickles)*29 + knuts


if __name__ == '__main__':
    main()

def main():
    coins_list = [100, 50, 25]
    list_total = total(*coins_list)
    print(f'Total: {list_total} knuts')

    coins_dict = {'galleons': 100, 'sickles': 50, 'knuts': 25}
    dict_total = total(**coins_dict)
    print(f'Total: {dict_total} knuts')


def total(galleons: int, sickles: int, knuts: int):
    return (galleons*17 + sickles)*29 + knuts


if __name__ == '__main__':
    main()

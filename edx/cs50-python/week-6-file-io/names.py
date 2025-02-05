from typing import List


def main():
    names: List[str] = []
    with open('names.txt', 'r') as file:
        for line in file:
            names.append(line.rstrip())
    for name in sorted(names):
        print(f'Hello, {name.title()}')


def read_file(file_path: str) -> List[str]:
    lines: List[str] = []
    with open(file_path, 'r') as file:
        for line in file:
            lines.append(line)
    return lines


def append_file(file_path: str, inputs: List[str]) -> None:
    with open(file_path, 'a') as file:
        for input in inputs:
            file.write(input)
    return


if __name__ == '__main__':
    main()

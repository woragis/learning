def main():
    words = ['harry', 'ron', 'hermione', 'draco']
    '''
    # List Comprehension
    Function if it wasn't through list comprehension:
    for name in words:
        if len(name) > 3:
            big_names.append(name)
    '''
    big_names = [name for name in words if len(name) > 3]
    print(big_names)

    '''
    # Dict Comprehension
    for word in big_names:
        if word in counts:
            counts[word] += 1
        else:
            conuts[word] = 1
    '''
    counts = {name: words.count(name) for name in big_names}
    print(counts)


if __name__ == '__main__':
    main()

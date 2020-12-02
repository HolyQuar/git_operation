if __name__ == '__main__':
    # one:prefixing the string with f or F,
    # An optional format specifier can follow the expression.
    import math

    str_1 = f'The value of pi is approximately {math.pi:.3f}.'
    print('str_1:', str_1)

    # This is useful for making columns line up.
    # Passing an integer after the ':' will cause that field to be a minimum number of characters wide.
    table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
    for name, phone in table.items():
        # 5--all_nameCharacter_num
        #10d:phone_num
        print(f'{name:8}==>{phone:8d}')

    # convert the value before it is formatted
    """
    '!a' applies ascii(), '!s' applies str(), and '!r' applies repr():
    """
    animals = 'eels'
    print(f'My hovercraft is full of {animals}')
    print(f'My hovercraft is full of {animals !s}')
    print(f'My hovercraft is full of {animals !r}')
    print(f'{"a"!a}')

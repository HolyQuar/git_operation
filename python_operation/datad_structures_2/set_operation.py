if __name__ == '__main__':
    # Curly braces or the set() function can be used to create sets
    basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
    print(basket)
    print('orange' in basket)

    # set operations
    a = set('abracadabra')
    b = set('alacazam')
    print(a)
    print(b)
    # letters in a but not in b
    print(a-b)
    # letters in a or b or both
    print(a|b)
    # letters in both a and b
    print(a&b)
    # letters in a or b but not both
    print(a^b)

    letters={x for x in 'a;fas;f;f;abra' if x not in 'abc'}
    print(letters)
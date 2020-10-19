if __name__ == '__main__':
    print('We are the {} who sya "{}"!'.format('knights', 'Ni'))
    # A number in the brackets can be used to refer to the position of the object passed into the str.format() method.
    print('{0} and {1}'.format('spam', 'eggs'))
    print('{1} and {0}'.format('spam', 'eggs'))

    # use  keyword arguments
    print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

    # Positional and keyword arguments can be arbitrarily combined:
    print('The story of {0},{1},and {other}.'.format('Bill', 'Manfred', other='Georg'))

    # long format string
    table = {'one': '1', 'two': 2, 'three': 3}
    print('one:{one:s};three:{three:d};two:{two:d};'.format(**table))

    # produce a tidily-aligned set of columns
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x ** 2, x * x * x))

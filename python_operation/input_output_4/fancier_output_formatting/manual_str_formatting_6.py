if __name__ == '__main__':
    # repr()--
    """
    Note that the one space between 
    each column was added by the way print() works
    """
    for x in range(1, 11):
        print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
        # are similar methods str.ljust() and str.center().
        print(repr(x * x * x).rjust(4))
    # {}.format
    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x ** 2, x * x * x))

    """
    The str.rjust() method of string objects right-justifies a string 
    in a field of a given width by padding it with spaces on the lef.
    --there are similar methods str.ljust() and str.center().
    """

    """
    str.zfill(), which pads a numeric string on the left with zeros. 
    It understands about plus and minus signs
    """
    num_one='12'.zfill(5)
    print('num_one:{}'.format(num_one))
    print('num_one_type:{}'.format(type(num_one)))
    # specify character_num
    print(f'{num_one:6}==')
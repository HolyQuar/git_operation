if __name__=='__main__':
    """
    The comparison operators in and not in check whether a value occurs (does not occur) in a sequence.
    The operators is and is not compare whether two objects are really the same object;
    this only matters for mutable objects like lists. All comparison operators have the same priority, 
    which is lower than that of all numerical operators.
    Comparisons can be chained. For example, a < b == c
    the Boolean operators and and or, have lower priorities than comparison operators;
    not has the highest priority and or the lowest, so that A and not B or C is equivalent to (A and (not B)) or C.
    """

    string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
    non_null=string1 or string2 or string3
    print(non_null)
    # Some examples of comparisons between sequences of the same type:
    a=(1, 2, 3) < (1, 2, 4)
    print(a)
    b=[1, 2, 3] < [1, 2, 4]
    print('b:{}'.format(b))
    c='ABC' < 'C' < 'Pascal' < 'Python'
    print('c:{}'.format(c))
    d=(1, 2, 3, 4) < (1, 2, 4)
    print('d:{}'.format(d))
    e=(1, 2) < (1, 2, -1)
    print('e:{}'.format(e))
    f=(1, 2, 3) == (1.0, 2.0, 3.0)
    print('f:{}'.format(f))
    g=(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)
    print('g:{}'.format(g))

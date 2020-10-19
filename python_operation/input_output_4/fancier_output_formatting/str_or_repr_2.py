if __name__ == '__main__':
    """the same :
    numbers or structures like lists and dictionaries
    """
    s = 'Hello, world.'
    # The str() function is meant to return representations of values which are fairly human-readable,
    s1 = str(s)
    print(type(s1))
    print(s1)
    # repr() is meant to generate representations which can be read by the interpreter
    s2 = repr(s)
    print(type(s2))
    print(s2)

    num_str = str(1 / 7)
    print(num_str)

    x = 10 * 3.25
    y = 200 * 200
    compute_result = 'the value of x is {}, and y is {}'.format(repr(x), repr(y))
    print(compute_result)

    # The repr() of a string adds string quotes and backslashes
    hello = 'hello, world\n'
    print('hello:', hello)
    # original_str
    hellos = repr(hello)
    print('repr_hello:{}'.format(hellos))
    # The argument to repr() may be any Python object
    object_str = repr(([x, y,] ,('spam', 'eggs')))
    print('object:', object_str)

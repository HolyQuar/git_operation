if __name__=='__main__':
    # A tuple consists of a number of values separated by commas
    t = 12345, 54321, 'hello!'
    one=t[0]
    print(one)
    print(t)
    # nested:
    u = t, (1, 2, 3, 4, 5)
    print(u)
    # Tuples are immutable:
    # t[0] = 88888  # --error
    ## but they can contain mutable objects:
    v = ([1, 2, 3], [3, 2, 1])
    print(v)
    # the construction of tuples containing 0 or 1 items
    empty = ()
    singleton = 'hello',  # <-- note trailing comma
    print(len(empty))
    print(len(singleton))

    # tuple packing
    t = 12345, 54321, 'hello!'
    print(t)

    # unpacked
    x, y, z = t
    print(x)
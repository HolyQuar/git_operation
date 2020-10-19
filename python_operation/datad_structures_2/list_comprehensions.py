if __name__ == '__main__':
    # calculate squares-- x that still exists after the loop completes
    squares = []
    for x in range(10):
        squares.append(x ** 2)
    print(squares)

    # calculate the list of squares without any side effects using:
    squares_2 = list(map(lambda x: x ** 2, range(10)))
    print(squares_2)
    # equivalently
    squares_3 = [x ** 2 for x in range(10)]
    print(squares_3)

    """
    A list comprehension consists of brackets containing 
    an expression followed by a for clause, then zero or 
    more for or if clauses.
    """
    liscomp = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
    print(liscomp)
    # it’s equivalent to:
    combs = []
    for x in [1, 2, 3]:
        for y in [3, 1, 4]:
            if x != y:
                combs.append((x, y))
    print('combs:', combs)

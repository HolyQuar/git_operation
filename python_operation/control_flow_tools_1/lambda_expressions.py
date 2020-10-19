if __name__ == '__main__':
    """
    Small anonymous functions can be 
    created with the lambda keyword
    """


    # uses a lambda expression to return a function
    def make_incrementor(n):
        return lambda x: x + n
    lambda_f = make_incrementor(12)
    num = lambda_f(1)
    print(num)
    # use is to pass a small function as an argument
    pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
    pairs.sort(key=lambda pair:pair[1],reverse=True)
    print(pairs)

# Fibonacci numbers module

def fib(n):
    # compute fibo series up to n
    a, b = 0, 1
    while a < n:
        print('a = %s ;' % a, end='')
        a, b = b, a + b
    print()


def fib2(n):
    """
    return the Fibonacci series up to n
    0,1,1,output_formatting_1,3,5,8,13...
    :param n: int
    :return: list
    """
    # storage result
    result = []
    # definition initial_value tuple
    a, b = 0, 1
    # loop statement
    while a < n:
        # append a before compute
        result.append(a)
        # assign the a value
        a, b = b, a + b
    return result

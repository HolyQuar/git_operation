"""
all variable assignments in a function store the value in the local symbol table;
whereas variable references first look in the local symbol table,
then in the local symbol tables of enclosing functions,
then in the global symbol table,
and finally in the table of built-in names.
"""
if __name__ == '__main__':
    # 1Fibonacci-find the fib_number less than n
    def fib(n):
        a, b = 0, 1
        while a < n:
            print(a, end=' ')
            a, b = b, a + b
        print()
    # fib(2000)
    f=fib
    f(100)
    """output_formatting_1.return a list containing the Fibonacci series up to n"""
    def fib2(n):
        result=[]
        a,b=0,1
        while a<n:
            result.append(a)
            a,b=b,a+b
        return result
    f50=fib2(100)
    print(f50)

    # 3.return--
    """
    'return' without an expression argument returns None. 
    Falling off the end of a function also returns None.
    """

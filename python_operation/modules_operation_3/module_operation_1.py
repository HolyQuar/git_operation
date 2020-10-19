"""
import the existed module
"""
from python_operation.modules_operation_3 import fibo_0

if __name__ == '__main__':
    # Using the module name you can access the functions:
    num = fibo_0.fib(1000)
    print('num:', num)
    num1 = fibo_0.fib2(500)
    print('num1:', num1)

    # If you intend to use a function often you can assign it to a local name:
    new_fib = fibo_0.fib
    print(new_fib(50))
    from python_operation.modules_operation_3.fibo_0 import fib, fib2
    print(fib2(5))

    """
    This imports all names except those beginning with an underscore (_). 
    In most cases Python programmers do not use this facility since it introduces 
    an unknown set of names into the interpreter, possibly hiding some things you
    have already defined.
    """
    from python_operation.modules_operation_3.fibo_0 import *
    # If the module name is followed by as, then the name following as is bound directly to the imported module.
    from python_operation.modules_operation_3 import fibo_0 as fib
    print(fib.fib(50))

    # each module is only imported once per interpreter session.
    #  if it’s just one module you want to test interactively, use importlib.reload(), e.g. import importlib; importlib.reload(modulename).




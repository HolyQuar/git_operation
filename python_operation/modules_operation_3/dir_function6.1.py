import sys

from python_operation.modules_operation_3 import fibo_0

if __name__ == '__main__':
    """
    The built-in function dir() is used to find out which names a module defines;
    It returns a sorted list of strings:
     
    """
    fibo_0_list = dir(fibo_0)
    print(fibo_0_list)
    print('----------------------------')
    print('builtins:', fibo_0.__builtins__)
    print('doc:', fibo_0.__doc__)
    print('file:', fibo_0.__file__)
    print('loader:', fibo_0.__loader__)
    print('name:', fibo_0.__name__)
    print('package:', fibo_0.__package__)
    print('spec:', fibo_0.__spec__)

    # dir(sys)
    print('sys:', dir(sys))
    # dir()
    a = [1, 2, 3, 4, 5]
    print(dir())

    """
    dir() does not list the names of built-in functions and variables. 
    If you want a list of those, they are defined in the standard module builtins:
    """
    import builtins
    print('builtins:',dir(builtins))
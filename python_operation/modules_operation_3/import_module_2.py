if __name__=='__main__':
    import importlib
    from python_operation.modules_operation_3 import fibo_0
    fibo_import=importlib.reload(fibo_0)
    print('--------------------------')
    print(getattr(fibo_import,'fib2')(10))
    fibo_import_module=importlib.import_module('fibo','python_operation.modules_operation_3')
    print(getattr(fibo_import, 'fib2')(10))
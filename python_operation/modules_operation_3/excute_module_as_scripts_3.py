import importlib

if __name__=='__main__':
    import sys
    # definition the param for the excute module
    fibo_import_module=importlib.import_module('fibo','python_operation.modules_operation_3')
    print(fibo_import_module.fib2(int(sys.argv[1])))

    """
    -->(base) D:\Pycharm\Workspace\git_operation\python_operation\modules_operation>
        -->python excute_module_as_scripts_3.py 50
    """

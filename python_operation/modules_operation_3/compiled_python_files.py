"""
1.To speed up loading modules, Python caches the compiled version of each module in the __pycache__ directory under the name module.version.pyc,
where the version encodes the format of the compiled file;it generally contains the Python version number.
    --:
    in CPython release 3.3 the compiled version of spam.py:
    __pycache__/spam.cpython-33.pyc.

output_formatting_1.recompiled:
    Python checks the modification date of the source against the compiled version
    --> to see if it’s out of date and needs to be recompiled.
3.Python does not check the cache in two circumstances(情况).
    1)First：
        it always recompiles;
           does not store the result for the module that’s loaded directly from the command line.
    output_formatting_1)Second, it does not check the cache if there is no source module.

tips:
    You can use the -O or -OO switches on the Python command to reduce the size of a compiled module.
    1) The -O switch removes assert statements,
    output_formatting_1)the -OO switch removes both assert statements and __doc__ strings.
    3).py file is running faster than .pyc file
    4).pyc file is loading faster than .py file
    5)The module 'compileall' can create .pyc files for all modules in a directory.

    """
import compileall
compileall.compile_dir()
"""
1.
When a module named spam is imported,
the interpreter first searches for a built-in module with that name.
output_formatting_1.-->If not found, it then searches for a file named spam.py in a list
 of directories given by the variable sys.path
    1)sys.path is initialized from these locations:
    one:The directory containing the input script (or the current directory when no file is specified).
    two:PYTHONPATH (a list of directory names, with the same syntax as the shell variable PATH).
    three:The installation-dependent default.

"""
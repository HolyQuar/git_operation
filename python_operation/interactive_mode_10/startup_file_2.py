""" If you want to use the startup file in a script, you must do this explicitly in the script:"""
import os
filename = os.environ.get('PYTHONSTARTUP')
if filename and os.path.isfile(filename):
    with open(filename) as fobj:
        startup_file = fobj.read()
    exec (startup_file)
#exec--execute the much_code
x = 'name = "Bill"\nprint(name)'
exec(x)
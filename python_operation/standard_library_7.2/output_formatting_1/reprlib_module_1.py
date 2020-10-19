"""
The reprlib module provides a version of repr() customized
-for abbreviated displays of large or deeply nested containers:
"""
import reprlib
set_abbreviated_display=reprlib.repr(set('upercalifragilisticexpialidocious'))
print('set_abbreviated_display:{}',format(set_abbreviated_display))
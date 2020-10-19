if __name__ == '__main__':
    # The try … except statement has an optional else clause
    """
     It is useful for code that must be executed 
     if the try clause does not raise an exception. 
    """
    import sys

    sys.argv.append('string_content.txt')
    print(sys.argv)

    for arg in sys.argv[1:]:
        print(arg)
        try:
            f = open(arg, 'r')
        except OSError:
            print('cannot open: {}'.format(arg))
        else:
            print(arg, 'has', len(f.readlines()), 'lines.')
            f.close()

    # The variable is bound to an exception instance with the arguments stored in instance.args
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))
    print('inst_args:',inst.args)
    print(inst)

    x, y = inst.args
    print('x =', x)
    print('y =', y)
"""
if they occur inside functions that are called 
(even indirectly) in the try clause.
"""
def this_fails():
    x = 1/0


try:
    this_fails()
except ZeroDivisionError as err:
    print('Handing run-time error:',err)
print('------------------------------------------------')
"""
Raising Exceptions
"""
# raise NameError('HiThere')

"""
 If an exception class is passed, 
 it will be implicitly instantiated 
 by calling its constructor with no arguments
"""
# raise ValueError

"""
determine whether an exception was raised but don’t intend to handle it,

"""
print('------------------raise----------------------')
# the same exception will not be catched by twice.
# raise NameError('Hi')
# print('hello')
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by~')
    raise

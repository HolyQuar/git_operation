if __name__ == '__main__':
    class ComplexClass:
        def __init__(self, realpart, imagpart):
            """have arguments passed on to __init__()."""
            self.r = realpart
            self.i = imagpart

        def f(self):
            return 'hello world'
    x_class = ComplexClass(3.0, -4.5)
    print('x_class_attribute:{}'.format((x_class.r, x_class.i)))
    # There are two kinds of valid attribute names: data attributes and methods.

    # Data attributes
    """
    Data attributes need not be declared,
    - they spring into existence when they are first assigned to
    - like local variables
    """
    # assign 1 to x_class.counter
    x_class.counter = 1
    while x_class.counter < 10:
        x_class.counter = x_class.counter*2
    print('x.counter:{}'.format(x_class.counter))
    # delect the counter attribute
    del x_class.counter

    # method --a function that “belongs to” an object.
    # x_class.f is a valid method reference, since ComplexClass.f
    """
    a method is called right after it is bound
    """
    print(x_class.f())
    # x.f is a method object
    x_class_f=x_class.f
    while True:
        print(x_class_f())
    # the call x.f() is exactly equivalent to MyClass.f(x)
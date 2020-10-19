if __name__=='__main__':
    """
    class object is basically a wrapper around the contents of 
    the namespace created by the class definition"""
    class Myclass:
        """A simple example class"""
        int_num=123456
        def f(self):
            return 'hello world'
    # instantiation Class
    x = Myclass()
    # Myclass.int_num attribute:
    print('int_num attribute: {}'.format((x.int_num,type(x.int_num))))
    # assign the value for int_num--like change the statics attribute

    print('original_num:{}'.format(Myclass.int_num))
    Myclass.int_num = 123
    y = Myclass()
    print('y.int_num:{}'.format(y.int_num))
    print('x.int_num:{}'.format(x.int_num))
    # reference the f function:
    print('reference the f:{}'.format(x.f()))
    # reference the docstring values
    print('Myclass_docstring:{}'.format(Myclass.__doc__))
    print('Myclass.x_docstring:{}'.format(x.__doc__))
    # reference all dict_attribute
    print('dict_atribute:{}'.format(Myclass.__dict__))
    print('Myclass_init:{}'.format(Myclass.__init__))
    # lookup inheritance class
    print('Myclass_base:{}'.format(Myclass.__base__))
    print('class:{}'.format(x.__class__))
    print('class_dir:{}'.format(Myclass.__dir__))
    print('class_flags:{}'.format(Myclass.__flags__))
    print('class_x.hash:{}'.format(x.__hash__()))
    print('class_x.getattribute:{}'.format(x.__getattribute__('int_num')))
    print('class_x.str:{}'.format(x.__str__()))

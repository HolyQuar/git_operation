"""
Python has two built-in functions that work with inheritance:
-Use isinstance() to check an instance’s type:
 isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.

-Use issubclass() to check class inheritance:
 issubclass(bool, int) is True since bool is a subclass of int.
 However, issubclass(float, int) is False since float is not a subclass of int.

Multiple Inheritance, these properties make it possible to design reliable and extensible classes_6 with multiple inheritance.
https://www.python.org/download/releases/2.3/mro/.
"""
# class DerivedClassName(Base1, Base2, Base3):
#     <statement-1>
#     .
#     .
#     .
#     <statement-N>

# Private Variables--
"""
“Private” instance variables don’t exist in Python.
there is a convention that is followed by most Python code: 
- a name prefixed with an underscore
- that cannot be accessed except from inside an object 

Name mangling--about override ：
-Any identifier of the form __spam is 
 textually replaced with _classname__spam, 
 where classname is the current class name with leading underscore(s) stripped
-at least two leading underscores, at most one trailing underscore
"""
if __name__ == '__main__':
    """Name mangling is helpful for letting subclasses 
    override methods without breaking intraclass method calls. """


    class Mapping:
        def __init__(self, iterable):
            self.items_list = []
            self.__update(iterable)

        def update(self, iterable):
            for item in iterable:
                self.items_list.append(item)
        # private copy of original update() method
        __update = update

    class MappingSubclass(Mapping):

        def update(self, keys,values):
            """provides new signature for update() and does not
            break __init__()"""
            for item in zip(keys,values):
                self.items_list.append(item)
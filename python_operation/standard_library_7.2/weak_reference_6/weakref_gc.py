"""
Python does automatic memory management:
--reference counting for most objects and garbage collection to eliminate cycles.
--The memory is freed shortly after the last reference to it has been eliminated.
--The weakref module provides tools for tracking objects without creating a reference.
"""
import weakref,gc
class A:
    def __init__(self,value):
        self.value = value
    def __repr__(self):
        return str(self.value)

# create a reference
a = A(10)
d = weakref.WeakValueDictionary()
# does not create a reference
d['primary'] = a
# fetch the object if it is still alive
print('d.primary:{}'.format(d['primary']))
del a
gc.collect()
print('d.primary:{}'.format(d['primary']))

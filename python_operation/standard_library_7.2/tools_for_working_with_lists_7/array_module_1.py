"""
The array module provides an array() object
--that is like a list that stores only homogeneous data
--and stores it more compactly
"""
# shows an array of numbers stored as two byte unsigned binary numbers (typecode "H")
from array import array
a = array('H',[4000,10,700,22222])
sum_num = sum(a)
print('sum_num:{}'.format(sum_num))
sub_num = a[1:3]
print('sub_num:{}'.format(sub_num))
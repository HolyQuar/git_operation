"""
Generators are a simple and powerful tool for creating iterators:
-They are written like regular functions
-use the yield statement whenever they want to return data.
-Each time next() is called on it, the generator resumes where it left off
-Anything that can be done with generators can also be done with class-based iterators as described in the previous section(iterator

--the __iter__() and __next__() methods are created automatically.
-- the local variables and execution state are automatically saved between calls.

)
"""


def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]


# test generator_reverse
for char in reverse('golf'):
    print(char)

# generator expressions
"""
-Generator expressions are more compact
-tend to be more memory friendly than equivalent list comprehensions.
-less versatile than full generator definitions.
"""
# sum of squares
print('-----------------')
sum_num = sum(i * i for i in range(10))
print('sum_num:{}'.format(sum_num))
# dot product
xvec = [10, 20, 30]
yvec = [7, 5, 3]
dot_product = sum(x * y for x, y in zip(xvec, yvec))
print('dot_product:{}'.format(dot_product))
# sin_value range-0~90
from math import sin, pi

sine_table = {x: sin(x * pi / 180) for x in range(0, 91)}
print('sine_table:{}'.format(sine_table))
sine_30 = round(sine_table[30], 2)
print('sine_30:{}'.format(sine_30))

# unique_word

unique_word = set(word for line in open('string_content.txt', 'r') for word in line
                  .split())
num = 0
for _ in unique_word:
    num += 1
    print('unique_word:{}'.format((_, num)))
print('unique_nums:{}'.format(len(unique_word)))
print('unique_nums1:{}'.format(unique_word.__len__()))

# module.__dict
"""
Module objects have a secret read-only attribute called __dict__ 
-which returns the dictionary used to implement the module’s namespace
"""
print('------------module_dict-')
import python_operation.classes_6.generators_7 as current_module
print('module_dict_attribute:{}'.format(current_module.__dict__))
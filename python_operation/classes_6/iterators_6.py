"""
 the most container objects can be looped over using a for statement

"""
# list
for element in [1, 2, 3]:
    print('list_element: {}'.format(element))
# tuple
for element in (1, 2, 3):
    print('tuple_elements:{}'.format(element))
# dict
for key in {'one': 1, 'two': 2}:
    print('dict_key:{}'.format(key))

# string_char
for char in '123':
    print('string_char:{}'.format(char))
# file_string
print('----------------------------')
for line in open('string_content.txt','r'):
    print(line,end='')
print('-----------------------------------------')
#  the for statement calls iter() on the container object.
s = 'abc'
# iterator object
it=iter(s)
print(it)
print('next_method1:{}'.format(next(it)))
print('next_method2:{}'.format(next(it)))
print('next_method3:{}'.format(next(it)))


import random
# random an element from a list or tuple or sting
fruit_list=['apple','pear','banana']
choice = random.choice(fruit_list)
print('choice:{}'.format(choice))
# generator a new list which contain five elements which the apple is ten multiples than others.
new_fruit_list = random.choices(fruit_list,weights=[10,1,1],k=5)
print('new_fruit_list:{}'.format(new_fruit_list))
print('--------------------------------')
# sampling without replacement
"""sampling 10 nums from the range(100) """
sample_num = random.sample(range(100),10)
print('distinct_10_nums:{}'.format(sample_num))

# random float num--0~1
float_num = random.random()
print('float_num:{}'.format(float_num))
# random integer num from a range
integer_num = random.randrange(6)
print('integer_num:{}'.format(integer_num))
"""a deque() object that is like a list

--with faster appends and pops from the left side
--but slower lookups in the middle.
--use for implementing queues and breadth first tree searches
"""
from collections import deque



d = deque(['task1', 'task2', 'task3'])
d.append('task4')
print('Handling:{}'.format(d))
# popleft
print('Popleft_element:{}'.format(d.popleft()))
print('after_popleft:{}'.format(d))
print('Popright_element:{}'.format(d.pop()))
print('after_popright:{}'.format(d))
new_d = d.copy()
print('new_d:{}'.format(new_d))
while new_d.__len__()>0:
    new_d.pop()
else:
    print('new_d is None: {}'.format(new_d))
    # the original_d is not change
    print('original_d:{}'.format(d))
#  breadth first tree searches:
"""
lookup the goal document in the hierarchy_dir
"""
unsearched = deque(['starting_node_path'])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     while unsearched is not None:
#         for m in gen_move(node):
#             if is_goal(m):
#                 return m
#             # input the new dir to the unsearched_deque
#             unsearched.append(m)

"""
 provides functions for implementing heaps based on regular lists
 --The lowest valued entry is always kept at position zero.
 --use for accessing the smallest element but do not want to run a full list sort:
"""
from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# rearrange the list into heap order
heapify(data)
# add a new entry
pop_data=heappop(data)
print('pop_data:{}'.format(pop_data))
print('------------------')
heap_data = heappush(data, -5)
pop_data1=[heappop(data) for i in range(3)]
print('pop_data1:{}'.format(pop_data1))

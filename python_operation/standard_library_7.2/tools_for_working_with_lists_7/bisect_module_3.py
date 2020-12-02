"""the bisect module with functions

--for manipulating sorted lists.
"""
import bisect
scores = [(100,'perl'),(200,'tcl'),(400,'lua'),(500,'python')]
# insert to the list and sort the order ascending
bisect.insort(scores,(500,'ruby'))
print('new_score:{}'.format(scores))
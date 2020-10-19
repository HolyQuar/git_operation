if __name__=='__main__':
    """
    While appends and pops from the end of list are fast, 
    doing inserts or pops from the beginning of a list is slow 
    (because all of the other elements have to be shifted by one).
    
        To implement a queue, use collections.deque 
        which was designed to have fast appends and pops from both ends.
    """
    from collections import deque

    queue = deque(["Eric", "John", "Michael"])
    print(queue)
    queue.append("Terry")
    queue.append("Graham")
    print(queue)
    left_element=queue.popleft()
    print(left_element)
    print(type(left_element))
    #pop the last element
    print(queue.pop())
    print(queue)
    queue.appendleft('kellan')
    print(queue)


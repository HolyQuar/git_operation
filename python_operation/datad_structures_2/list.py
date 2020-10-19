if __name__ == '__main__':
    l = []
    l.append('a')
    print(l)
    l.extend([123, '12'])
    print(l)
    l.insert(0, 567)
    print(l)
    l.remove(123)
    print(l)
    # removes and returns the last item in the list.
    print(l.pop())
    print(l)
    # l.pop(index) Remove the item at the given position in the list, and return it
    print(l.pop(1))
    print(l)
    # Remove all items from the list. Equivalent to del a[:].
    l.clear()
    print(l)
    l.extend([123, '12', 'da', 'da', [1]])
    print(l)
    # index
    index = l.index('da', 0, 3)
    print(index)
    # count(object)
    print(l.count('da'))
    # sort
    s = [1, 2, 6, 21, 23, 12]
    s.sort(key=lambda x: x, reverse=True)
    print('desc:', s)
    print('origin:', s)
    # reverse
    # s.reverse()
    s1 = s.copy()
    s.sort()
    s[0] = 2
    s.append('a')
    s.append('z')
    s.append('n')
    print('s:', s)
    print('s1:', s1)

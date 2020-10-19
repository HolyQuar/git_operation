if __name__ == '__main__':
    a = [-1, 1, 66.25, 333, 333, 1234.5]
    del a[0]
    print(a)
    # remove slices from a list
    del a[2:4]
    print(a)
    # clear the entire list
    del a[:-1]
    print(a)
    # delete entire variables
    del a
    print(a)

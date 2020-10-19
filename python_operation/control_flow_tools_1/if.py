if __name__ == '__main__':
    #if ... elif ... elif ... else
    while True:
        x = int(input('please enter an integer:'))
        if x < 0:
            print('negative changed to zero')
        elif x ==2:
            exit(0)
        elif x == 0:
            print('Zero')
        elif x == 1:
            print('Single')
        else:
            print('More')

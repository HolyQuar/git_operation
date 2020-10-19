if __name__=='__main__':
    squares=[1,4,9,16,25]
    print(squares)

    print(squares[0])
    print(squares[-3:])
    print(squares[:])
    #concatenation_list
    print(squares+[23,22,12,121])
    #append_item
    squares.append(211)
    print(squares)
    #change_list
    squares[0]=123
    print(squares)
    #change slices_list
    letters=['a','b', 'c', 'd', 'e', 'f', 'g']
    print(letters)
    #change
    letters[2:5]=['C', 'D', 'E']
    print(letters)
    letters[2:5]=[]
    print(letters)
    letters[:]=[]
    print(letters)

    #len
    letters = ['a', 'b', 'c', 'd']
    print(len(letters))

    #nest list
    a = ['a', 'b', 'c']
    n = [1, 2, 3]
    x = [a, n]
    print(x)
    print(x[0][1])
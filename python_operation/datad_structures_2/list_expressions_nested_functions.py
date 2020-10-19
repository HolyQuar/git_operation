if __name__=='__main__':
    from math import pi
    pi_str=[str(round(pi,i)) for i in range(1,6)]
    print(pi_str)
    # Consider the following example of a 3x4 matrix
    # implemented as a list of 3 lists of length 4
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]
    # transpose rows and columns
    transpose_matrix=[[row[i] for row in matrix ]for i in range(4)]
    print(transpose_matrix)
    print('---------------------------------------')
    transpose_equivalent=[]
    for i in range(4):
        transpose_equivalent.append([row[i] for row in matrix])
    print(transpose_equivalent)

    transpose_equivalent_2 = []
    for i in range(4):
        transpose_row=[]
        for row in matrix:
            transpose_row.append(row[i])
        transpose_equivalent_2.append(transpose_row)
    print(transpose_equivalent_2)

    # prefer built-in functions to complex flow statements.
    # zip()
    zip_matrix=list(zip(*matrix))
    print('zip_matrix',zip_matrix)
    l=[]
    for matrixs in zip_matrix:
        # tuple --> list
        list_r=list(matrixs)
        l.append(list_r)
    print('zip:',l)

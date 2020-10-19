if __name__ == '__main__':
    vec = [-4, -2, 0, 2, 4]
    vec_squares = [x * 2 for x in vec]
    print(vec_squares)
    vec_positive = [x for x in vec_squares if x >= 0]
    print(vec_positive)
    vec_abs = [abs(x) for x in vec]
    print(vec_abs)
    print('-----------------------------------------------')
    # call a method on each element
    freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
    fruit_strip=[weapon.strip() for weapon in freshfruit]
    print(fruit_strip)
    num_calculate=[(x,x**2) for x in range(6)]
    print(num_calculate)
    # flatten a list using a listcomp with two 'for'
    new_vec= [[1,2,3], [4,5,6], [7,8,9]]
    flatten_num=[num for num_list in new_vec for num in num_list]
    print(flatten_num)
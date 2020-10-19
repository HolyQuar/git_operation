if __name__ == '__main__':
    tel = {'jack': 4098, 'sape': 4139}
    tel['guido'] = 4127
    print(tel)
    print(tel['jack'])
    del tel['sape']
    print(tel)
    tel['irv'] = 4127
    print(tel)
    print(type(tel))
    print(list(tel))
    print(tel)
    print(sorted(tel))
    print('guido' in tel)
    print('jack' not in tel)
    # dict constructor
    dict_new = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print(dict_new)

    # dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:
    dict_expression = {x: x ** 2 for x in (2, 4, 6)}
    print(dict_expression)
    # When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments
    print(dict(hello='hello world~', world='one'))

    print('-----------------------------------------')
    # looping
    knights = {'gallahad': 'the pure', 'robin': 'the brave'}
    for k, v in knights.items():
        print(k, v)
    # enumerate()
    for i, v in enumerate(['tic', 'tac', 'toe']):
        print(i, v)
    # zip()
    questions = ['name', 'quest', 'favorite color']
    answers = ['lancelot', 'the holy grail', 'blue']
    for q,a in zip(questions,answers):
        print('What is your {0}? It is {1}.'.format(q,a))
    # To loop over a sequence in reverse
    for i in reversed(range(1,10,2)):
        print(i)
    # To loop over a sequence in sorted order,use the sorted() function
    # which returns a new sorted list while leaving the source unaltered.
    basket=['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
    for f in sorted(set(basket)):
        print(f)
    # it is often simpler and safer to create a new list instead.
    import math
    raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
    filter_data=[]
    for value in raw_data:
        if not math.isnan(value):
            filter_data.append(value)
    print(filter_data)
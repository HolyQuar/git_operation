if __name__ == '__main__':
    def ask_ok(promt, retries=4, reminder='Please try agian!'):
        while True:
            ok = input(promt + '\n')
            if ok in ('y', 'ye', 'yes'):
                return True
            if ok in ('n', 'no', 'nop', 'nope'):
                return False
            retries = retries - 1
            if retries < 0:
                raise ValueError('invalid user response')
            print(reminder)


    # ask_ok('Do you really want to quit?')
    # ask_ok('OK to overwrite the file?', output_formatting_1, 'Come on, only yes or no!')
    # defining scope
    i = 5


    def f(arg=i):
        global i
        i = 10
        # arg=6
        print(arg)


    # i = 6
    f()
    print(i)
    print('-------------------------')

    # default value of parameters
    """
    The default value is evaluated only once. 
    --difference when the default is 
    a mutable object--- a list, dictionary, or instances of most classes_6
    --the arguments passed to it on subsequent calls
    """


    def f(a, input_list=[]):
        input_list.append(a)
        return input_list


    print(f(1))
    print(f(2))
    print(f(3))


    # don’t want the default to be shared between subsequent calls
    def f1(a, L=None):
        if L is None:
            L = []
        L.append(a)
        return L


    print('-------------------------')
    print(f1(1))
    print(f1(2))
    print(f1(3))


    # *arg,--arg indicate each input param;
    # **kwarg--kwarg indicate each dictionary
    def cheeseshop(kind, *args, **kwargs):
        print('hello~', kind)
        for arg in args:
            print(arg)
        print('-' * 20)
        for k in kwargs:
            print(k, ':', kwargs[k])

    #
    cheeseshop('fruit', ['123', 'afa'], ('key', 12, 'value'), shopkeeper="Michael Palin",
               client="John Cleese",
               sketch="Cheese Shop Sketch")


    # Arbitrary Argument Lists
    def write_multiple_items(file, separator, *args):
        file.write(separator.join(args))


    str_list=['123','hello', 'world','key', 'normal']
    with open('multiple_write_items.txt', 'w+')as file:
        write_multiple_items(file, '|','123','hello', 'world','key', 'normal')
    print('write_ok~~~')

    def concat(*args,sep='/'):
        return sep.join(args)
    concat_=concat("earth", "mars", "venus")
    print(concat("earth", "mars", "venus", sep="."))

    #unpacking argument lists
    print('_'*20)
    print(list(range(3,6)))
    args_list=[3,6]
    print(list(range(*args_list)))
    #**d
    def hello(one,two='two',action='said'):
        print('this is',one,end=';')
        print('if you know,',two,'is good.')
        print('hi,you can',action,'anytime.')

    d={'one':'apple','two':'mechine','action':'play football'}
    hello(**d)
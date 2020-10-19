if __name__=='__main__':
    def scope_test():
        def do_local():
            """
            attempt to change the scope.spam;--the spam variable should assignment first.
            :return:don't change the scope.spam value
            """
            spam = 'local spam'
        def do_nonlocal():
            """
            change the scope.spam
            --spam shaould assign fist
            :return: new local value
            """
            nonlocal spam
            spam = 'nonlocal spam'
        def do_global():
            """
            don't change the original scope.spam,assign new value in the global
            :return:new global value
            """
            global spam
            spam = 'global spam'
        # denifition test variable
        spam = 'test spam'
        print('scope_function attribute :spam={}'.format(spam))
        # attemp to change the local value
        do_local()
        print('after local assignment--don\'t change:scope.spam= {}'.format(spam))
        do_nonlocal()
        print('after non_local assignment--change the scope.spam:scope.spam= {}'.format(spam))
        do_global()
        print('after global assignment--don\'t change the scope.spam:scope.spam= {}'.format(spam))
        print('--------------------------------------')
        print('after non_local,scope.spam: scope.spam ={}'.format(spam))

        spam = 'change the value'
        print('re-assignment_spam,only change the current_local_scope value: spam = {}'.format(spam))
    scope_test()
    print('after global scope.attribute --In global scope:spam= {}'.format(spam))
    """
    minimizes the chance of conflict--Data attributes override method attributes
    using verbs for methods and nouns for data attributes
    """
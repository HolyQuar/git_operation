if __name__ == '__main__':
    """In real world applications, the finally clause is useful
     for releasing external resources (such as files or network connections), regardless of whether the use of the resource was successful.
    
    """
    # try:
    #     print('Hello world~')
    #     raise KeyboardInterrupt
    # finally:
    #     print('Goodbye,world~')
    """output_formatting_1.points:
     one:If an exception occurs during execution of the try clause, 
     the exception may be handled by an except clause.
     two:If an exception could occur during execution of an except or else clause,
     the exception is re-raised after the finally clause has been executed. 
     three:If the try statement reaches a break, continue or return statement, 
     the finally clause will execute just prior to the break, continue or return statement’s execution.
     four:If a finally clause includes a return statement, the returned value will be the one 
     from the finally clause’s return statement, not the value from the try clause’s return statement.
    """


    def divide(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            print('division by zero~')
        else:
            print('result is : {}'.format(result))
            # return result
        finally:
            print('executing finally clause~')


    # usual execute-->
    # if have the return clause:
    #   try-->else-->finally-->return result
    # else:try-->else-->finally
    print('divide_result:', divide(2, 1))
    print('--------------one--------------')
    # one:except-->finally
    divide(2, 0)
    # two:finally-->re-raise exception
    print('---------------two----------------')
    # divide('output_formatting_1','1')

    print('--------------predefined-----------------')
    # 3.predefined clean-up actions
    """After the statement is executed, the file f is 
    always closed, even if a problem was encountered while processing the lines.
    use:Some objects define standard clean-up actions to be undertaken when the object is no longer needed, 
    regardless of whether or not the operation using the object succeeded or failed
    """
    with open('exception.txt','r') as f:
        for line in f:
            print(line,end='')

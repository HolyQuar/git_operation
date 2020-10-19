if __name__ == '__main__':
    """
    asks the user for input until a valid integer has been entered, 
    but allows the user to interrupt the program (using Control-C or whatever the operating system supports)
    """
    while True:
        try:
            # x = int(input('Please enter a number: '))
            # if input the right param
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
    # a class in an except clause
    class B(Exception):
        pass
    class C(B):
        pass
    class D(C):
        pass
    for cls_e in [B, C, D]:
        # B is the base class--B,C,D;
        # except B first--B,B,B
        try:
            raise cls_e()
        except D:
            print("D")
        except C:
            print("C")
        except B:
            print("B")

    # The last except clause may omit
    import sys

    try:
        with open('exception.txt') as f:
            str_line=f.readline()
            i=int(str_line.strip())
            # res=i/0
    except OSError as err:
        print('OS error: {}'.format(err))
    except ValueError:
        print('Could not convert data to an integer.')
    except:
        print('Unexpected error: {}'.format(sys.exc_info()[0]))
        raise


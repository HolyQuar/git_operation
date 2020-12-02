# -*- coding:utf-8 -*-


def fn(*args, **kwargs):
    num = 0
    for i in args:
        num +=i
    for i in kwargs.values():
        num += i
    return num

def A(fn):
    print(1)

def run():
    print(2)
    fn()
    print('a')
    return run


def B(fn):
    print(3)




def C(fn):
    print(5)
    fn()




@A
@B
@C
def test():
    print(7)

if __name__ == '__main__':
    test()

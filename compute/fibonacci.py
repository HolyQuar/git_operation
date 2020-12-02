def fibonacci(num):
    a,b=0,1
    if num==1:return 0
    elif num==2:return 1
    else:
        index=0
        while index<num:
            print(a)
            a,b=b,a+b
            index+=1
        return b

if __name__=='__main__':
    result=fibonacci(3)
    print('result:',result)
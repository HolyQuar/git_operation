# -*- conding: encoding -*-
if __name__ == '__main__':
    # measure string
    words = ['cat', 'window', 'defenestrate']
    for w in words:
        print(w, len(w))
    # Loop over a slice copy of the entire list
    for w in words[:]:
        if len(w) > 6:
            words.insert(0, w)
    print(words)
    words.reverse()
    print(words)
    print(words.index('cat'))
    words.sort()
    print(words)
    print(words.count('defenestrate'))
    words.extend(['hello'])
    print(words)
    sorted(words)
    print(words)

    # range
    for i in range(5):
        print(i)
    print('***************')
    print(type(range(5, 10)))
    for i in range(5, 10):
        print(i)
    print('***************')
    for i in range(0, 10, 3):
        print(i)
    print('***************')
    for i in range(-10, -100, -30):
        print(i)
    # combine range() and len() as follows
    str_list = ['Mary', 'had', 'a', 'little', 'lamb']
    for i in range(len(str_list)):
        print(i, str_list[i])
    # enumerate
    print('*************')
    for i, v in enumerate(str_list):
        print(i, v)
    print(list(range(5, 10)))

print('---------break,else statements-------------------')
# break and continue statements,and else clauses on loops
# else--look for prime numbers
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n // x)
        # break out-not excute the else clasuses statement
        break
    else:
        # n is a prime number
        print(n, 'is a prime number.')
#continue-- borrowed from C, continues with the next iteration of the loop:
print('--------continue----------------')
for num in range(2,10):
    if num%2==0:
        print('Found an even number',num)
        continue
    else:
        print('Found a number:',num)


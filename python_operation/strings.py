if __name__ == '__main__':
    """
    strings cannot be changed — they are immutable.
    """
    print('spam eggs')
    print("doesn't")
    print('"yes",they said')
    print('\"yes\",they said')
    print('"Isn\'t,"they said')

    s = 'First line.\nSecond line.'
    print(s)
    # r--\-->normal
    print('C:\some\name')
    print(r'C:\some\name', end='\n')
    # multiple lines
    print("""
    Usage: thingy [OPTIONS]
         -h                        Display this usage message
         -H hostname               Hostname to connect to
    """)
    # concatenated
    print(3 * 'un' + 'ij')
    print('py' 'thon')

    text = ('Put several strings within parentheses '
            'to have them joined together.')
    print(text)

    s='python'
    print('j'+s[1:])

    #len(str)
    print(len(s))

    string='hello world~~'
    new_str=string[1:]
    print(string)
    print(new_str)
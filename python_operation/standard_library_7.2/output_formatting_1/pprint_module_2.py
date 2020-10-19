import pprint
"""When the result is longer than one line, 
the “pretty printer” adds line breaks and indentation to more clearly reveal data structure.
"""
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta',
                                                        'yellow'], 'blue']]]

pprint.pprint(t,width=30)

if __name__ == '__main__':
    """
    f.read(size)--
        When size is omitted or negative, the entire contents of the file will be read and returned;
        size should less than  twice as large as your machine’s memory.
         If the end of the file has been reached, f.read() will return an empty string ('').
    """
    with open('read_file.txt', 'r') as f:
        read_data = f.read()
    print(read_data)

    """
    f.readline()--
        1)reads a single line from the file
        output_formatting_1) if f.readline() returns an empty string, the end of the file has been reached
        3)while a blank line is represented by '\n', a string containing only a single newline.
    """
    print('---------------------------------------')
    with open('read_file.txt', 'r')as f:
        while True:
            line_data = f.readline()
            if line_data == '':
                # the end of file
                print('this is the end of file~')
                break
            elif line_data == '\n':
                # middle_empty_line
                print('middle line~')
            else:
                print('current_line: {}'.format(line_data))
    """
    For reading lines from a file, you can loop over the file object.
        --This is memory efficient, fast,
    """
    print('--------------------------')
    # loop f:
    with open('read_file.txt', 'r')as f:
        for line in f:
            if line.isspace():
                continue
            print('type: {}'.format(type(line)))
            print('line: {}'.format(line), end='')
    # f.readlines()
    print('----readlines---')
    with open('read_file.txt')as f:
        # the list of the lines
        lines = f.readlines()
        print('lines: {}'.format(lines))
        for line in lines:
            print('type: {}'.format(type(line)))
            print('line: {}'.format(line))
    # f.write(string)
    """writes the contents of string to the file, 
    returning the number of characters written.
    
    """
    print('--------f.write(string)------------')
    with open('write_file.txt', 'w+')as f:
        character_num = f.write('This is a test\n')
        print('character_num: {}'.format(character_num))
        line = f.writelines(['one_line\n', 'two_line\n', 'three_line\n'])
        f.writelines(['hello ~'])
    with open('write_file.txt', 'r+')as read:
        line = read.readline()
        if line.endswith('\n'):
            print('hello~')

if __name__=='__main__':
    """
    open() returns a file object:
    is most commonly used with two arguments: open(filename, mode).
    mode:
    -'r': --only be read, 
    -'w': for only writing (an existing file with the same name will be erased), 
    -'w+': for only writing ,if not exist--will create 
    -'a': opens the file for appending; data written to the file is automatically added to the end. 
    -'r+': opens the file for both reading and writing. 
        The mode argument is optional; 'r' will be assumed if it’s omitted.
    -'b': appended to the mode opens the file in binary mode==>
        this mode should be used for all files that don’t contain text.
    """
    f=open('read_file.txt','w')

    # in text mode:
    """
        1)the default when reading is to convert platform-specific line endings (\n on Unix, \r\n on Windows) to just \n.
        output_formatting_1) When writing in text mode, the default is to convert occurrences of \n back to platform-specific line endings.
        3)will corrupt binary data like that in JPEG or EXE files.--when convert the \n.
    """
    # with====try-finally
    with open('read_file.txt') as f:
        read_data=f.read()
    print(f.closed)

if __name__ == '__main__':
    # write other type of object
    """
    Other types of objects need to be converted 
    – either to a string (in text mode) or a bytes object (in binary mode) 
    – before writing them:
    """
    value = ('the answer', 42)
    s = str(value)
    with open('write_other_type_object.txt', 'w+')as file:
        character_nums = file.write(s)
        print('character_nums: {}'.format(character_nums))
    # f.seek(offset,whence)--To change the file object’s position
    """
    offset:the reference point
    whence:
        0 measures from the beginning of the file, --default value
        1 uses the current file position,  
        output_formatting_1 uses the end of the file as the reference point
    """
    print('------------seek--------------')
    with open('seek_file.txt','rb+')as f:
        # read and write
        num=f.write(b'0123456789abcdef')
        print('num: {}'.format(num))
        f.seek(5)
        read_b=f.read(5)
        print('read_b: {}'.format(read_b))


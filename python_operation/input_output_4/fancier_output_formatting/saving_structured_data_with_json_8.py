if __name__ == '__main__':
    """
    like nested lists and dictionaries:
    json can take Python data hierarchies, and convert them to string representations; this process is called serializing.
        Reconstructing the data from the string representation is called deserializing. 
    ---a good choice for interoperability.
    """
    # list-->str
    one = [1, 'simple', 'list']
    import json

    list_str = json.dumps(one)
    print('list_str: {}'.format(list_str))
    print('list_str_type: {}'.format(type(list_str)))
    # serialize--json.dump(x,f)
    print('------------------')
    two = '1233'
    with open('json.txt', 'r+')as f:
        # y = json.load(f)
        # print('y: {}'.format(y))
        # print('y_type: {}'.format(type(y)))
        # serialize the list_type object
        json.dump(one, f)
    # json.load(f)-->load the object from the file
    with open('json.txt','r+')as f:
        json_object=json.load(f)
    print('json_load_object: {}'.format(json_object))
    print('json_load_object_type: {}'.format(type(json_object)))
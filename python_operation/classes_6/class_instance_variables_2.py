if __name__ == '__main__':
    """ 
    1.instance variables are for data unique to each instance 
    output_formatting_1.and class variables are for attributes and methods shared by all instances of the class
    """


    class Dog:
        kind = 'canine'
        # mistaken use of a class variable
        tricks = []
        def __init__(self, name):
            self.name = name
        def add_trick(self,trick):
            self.tricks.append(trick)
    d = Dog('Fido')
    e = Dog('Buddy')
    # Dog class attribute--all the same:
    print('attribute_value:{}'.format((d.kind,e.kind)))
    # instance variables
    print('d.name:{}'.format(d.name))
    print('e.name:{}'.format(e.name))
    print('-----------------------------------')
    d.add_trick('roll over')
    e.add_trick('play dead')
    print('d_trick--all_tricks:{}'.format(d.tricks))
    # use an instance variabl instead
    class InstanceDog:
        kind = 'canine'
        # mistaken use of a class variable
        def __init__(self, name):
            self.tricks = []
            self.name = name
        def add_trick(self,trick):
            self.tricks.append(trick)
    dog = InstanceDog('One')
    dog2 = InstanceDog('Two')
    dog.add_trick('hello')
    dog2.add_trick('world')
    print('dog_tricks:{}'.format(dog.tricks))
    print('dog2_tricks:{}'.format(dog2.tricks))
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        print('this is init.')
        self.data = data
        self.index = len(data)

    def __iter__(self):
        print('this is iter.')
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        # obtain the backward_index
        self.index -= 1
        print('this is next.index = {}'.format(self.index))
        return self.data[self.index]


rev = Reverse('spam')
# iter
print('rev_iter:{}'.format(iter(rev)))
print('--------------------------------')
for char in rev:
    # quote:iter-->__next__()---  each one at a time
    print('reverse_element:{}'.format(char))




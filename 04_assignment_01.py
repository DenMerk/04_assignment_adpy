class MyIter:
    def __init__(self, iter_list):
        self.iter_list = iter_list
        self.unpacked_list = []
        self.index = 0

    def __iter__(self):
        self.iteration = self.iter_list
        for self.inner_list in self.iteration:
            for self.el in self.inner_list:
                self.unpacked_list.append(self.el)
        return self

    def __next__(self):
        self.index += 1
        if self.index > len(self.unpacked_list):
            raise StopIteration
        return self.unpacked_list[self.index - 1]


nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]

for item in MyIter(nested_list):
    print(item)

flat_list = [item for item in MyIter(nested_list)]
print(flat_list)
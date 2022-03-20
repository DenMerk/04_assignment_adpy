nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


def flat_generator(iter_list):
    unpacked_list = []
    for inner_list in iter_list:
        for el in inner_list:
            unpacked_list.append(el)
            yield el


for item in flat_generator(nested_list):
    print(item)

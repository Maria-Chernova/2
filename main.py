import types

def flat_generator(list_of_lists):
    index = 0
    inner_index = 0
    while index < len(list_of_lists):
        print(f"Start iteration {index + 1}, {inner_index}")
        if inner_index < len(list_of_lists[index]):
            item = list_of_lists[index][inner_index]
            inner_index += 1
            print(f"Yielding {item}")
            yield item
        else:
            index += 1
            inner_index = 0
            print(f"Moving to next inner list {index}")
    print("End of iteration")

def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

if __name__ == '__main__':
    test_2()


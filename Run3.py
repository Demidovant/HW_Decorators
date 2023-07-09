import types
import os
from Run2 import logger

log_path = 'Run3.log'


@logger(log_path)
def flat_generator(list_of_lists):
    for elem in list_of_lists:
        if isinstance(elem, list):
            for j in flat_generator(elem):
                yield j
        else:
            yield elem


@logger(log_path)
def test_4():
    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


if __name__ == '__main__':
    if os.path.exists(log_path):
        os.remove(log_path)
    test_4()

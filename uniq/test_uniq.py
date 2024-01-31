from uniq import uniq

import random


def test_1():
    output_list = uniq([2, 3, 1, 10, 3, 3, 1, 10, 5, 2])
    assert list(output_list) == [2, 3, 1, 10, 5]

def test_2():
    output_list = uniq([2, 2, 2, 2, 2, 2])
    assert list(output_list) == [2]

def test_speed():
    input_list = [random.randrange(10000) for _ in range(100000)]
    output_list = uniq(input_list)

    assert len(list(output_list)) < 10000

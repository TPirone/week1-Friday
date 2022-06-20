from utility.Exercise1 import sum_list


def test_sum_list_1():
    assert sum_list(10, 20) == 30


def test_sum_list_2():
    assert sum_list(10.1, 20.5) == 30.6


def test_sum_list_3():
    assert sum_list(10.1, -5) == 5.1


def test_sum_list_4():
    assert sum_list(10, 20, 30) == 60

def test_sum_test_5():
    assert sum_list("hello")
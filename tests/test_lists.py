def test_list_contains():
    data = [1, 2, 3]
    assert 2 in data


def test_list_append():
    data = [1, 2, 3]
    data.append(4)
    assert data == [1, 2, 3, 4]


def test_list_length():
    data = [1, 2, 3]
    assert len(data) == 3


def test_list_remove():
    data = [1, 2, 3]
    data.remove(1)
    assert data == [2, 3]


def test_list_pop_last():
    data = [1, 2, 3]
    value = data.pop()
    assert value == 3
    assert data == [1, 2]


def test_list_pop_first():
    data = [1, 2, 3]
    value = data.pop(0)
    assert value == 1
    assert data == [2, 3]


def test_sort_list():
    data = [3, 2, 1]
    data.sort()
    assert data == [1, 2, 3]
